import grpc
import random
import time
import threading

import sys
# sys.path.append("client_sensors")
import sensor_pb2
import sensor_pb2_grpc as rpc

import socket

MIN_SAFE_DIST = 5
TRACK_LENGTH = 30
STOP_POS = 30
TRAIN_SPEED = 1
UPDATE_RATE = 3

class TrainClient:
    def __init__(self, server_address=f'{socket.gethostbyname(socket.gethostname())}:50052'):
        self.train_id = None
        self.location = STOP_POS
        self.speed = TRAIN_SPEED
        self.channel = grpc.insecure_channel(server_address)
        self.conn = rpc.ServerStub(self.channel)

    def thread(self):
        if self.train_id is not None:
            # create new listening thread for when new message streams come in
            self.listener_thread = threading.Thread(target=self.__listen_for_alarms, daemon=True).start()
            self.run_thread = threading.Thread(target=self.run)
            self.run_thread.start()
            # self.run_thread.join()
    
    def __listen_for_alarms(self):
        if self.train_id is not None:
            n = sensor_pb2.TrainConnectRequest()
            n.train_id = self.train_id
            # continuously  wait for new messages from the server!
            for connectReply in self.conn.TrainSensorStream(n):  
                # if alarm, not reset
                if connectReply.alarm:
                    # display alarm message
                    print("From server: {}".format(connectReply.message)) 
                    # stop the train 
                    self.speed = connectReply.new_speed
                    self.update_status()
                else:
                    print("From server: Restart trains at speed {}".format(connectReply.message)) 
                    self.speed = int(connectReply.message)

    def signup(self, train_id):
        if train_id != '':
            n = sensor_pb2.SignupRequest(train_id=train_id) 
            reply = self.conn.Signup(n)
            if reply.success:
                self.train_id = train_id
            return reply
        
    def signout(self, train_id):
        n = sensor_pb2.SignoutRequest(train_id=train_id)
        reply = self.conn.Signout(n)
        if reply.success:
            self.train_id = None
        self.listener_thread.join()
        self.run_thread.join()
        return reply

    def get_status(self):
        request = sensor_pb2.TrainStatusRequest(train_id=self.train_id)
        response = self.conn.GetTrainStatus(request)
        return response

    def update_status(self):
        self.location = (self.location + self.speed * UPDATE_RATE) % TRACK_LENGTH
        if self.location == STOP_POS % TRACK_LENGTH:
            print(f"Train {self.train_id} is at the train stop")

        request = sensor_pb2.TrainUpdateRequest(
            train_id=self.train_id, 
            location=self.location, 
            speed=self.speed
        )
        try: 
            response = self.conn.UpdateTrainStatus(request)
            return response.success
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.CANCELLED:
                pass
            elif rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                pass
            else:
                print(f"Received unknown RPC error: code={rpc_error.code()} message={rpc_error.details()}")
        
    
    
    def is_safe_to_instantiate(self):
        other_train_ids = [1, 2, 3]
        other_train_ids.remove(self.train_id)

        train_statuses = []
        for other_train_id in other_train_ids:
            train_status = self.get_other_train_status(other_train_id)
            if train_status.train_id != -1:  # train has instantiated
                train_statuses.append(train_status)

        if not train_statuses: # no other trains on track
            return True

        for train_status in train_statuses:
            dist = min(abs(train_status.location - STOP_POS),
                       abs(STOP_POS % TRACK_LENGTH - train_status.location)) # Assuming the train will start at the stop
            if dist < MIN_SAFE_DIST:
                return False # if any are too close, then not safe

        return True
    
    def get_other_train_status(self, other_train_id):
        request = sensor_pb2.OtherTrainStatusRequest(
            requesting_train_id=self.train_id, 
            other_train_id=other_train_id
        )
        response = self.conn.GetOtherTrainStatus(request)
        return response


    def run(self):
        print(f'Train {self.train_id} waiting for instantiation...')

        while not self.is_safe_to_instantiate():
            time.sleep(1)

        print(f'Train {self.train_id} instantiated...')

        print(f'Train {self.train_id} started...')

        while True:
            # Update train status in Scheduler API
            update_success = self.update_status()
            if not update_success:
                print(f'Error updating train {self.train_id} status.')

            # Get train status from Scheduler API
            train_status = self.get_status()
            print(f'Train {self.train_id} status: location={train_status.location}, speed={train_status.speed}')

            time.sleep(UPDATE_RATE)  # Wait for some time before next update


if __name__ == '__main__':
    c = TrainClient()

    try:        
        while c.train_id is None:
            train_id = int(input("Enter train ID (1, 2, or 3) to instantiate a train or 0 to exit: "))
            if train_id in [1,2,3]:
                reply = c.signup(train_id)
                if reply.success:
                    print("Valid train ID!")
                else:
                    print("{}".format(reply.error))
            else:
                print("Invalid train ID. Please enter 1, 2, or 3.")
            c.thread()
    except KeyboardInterrupt: # catch the ctrl+c keyboard interrupt
        if c.train_id is not None:
            temp = c.signout()