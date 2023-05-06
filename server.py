import grpc
from concurrent import futures
import time
import queue

import sys
# sys.path.append("client_sensors")
import sensor_pb2
import sensor_pb2_grpc
import socket

MIN_SAFE_DIST = 5
TRACK_LENGTH = 30
STOP_POS = 30
TRAIN_SPEED = 1
UPDATE_RATE = 3

class Server(sensor_pb2_grpc.ServerServicer):
    def __init__(self):
        self.trains = {}  # Dictionary to store train status
        self.train_at_stop = False # updates if any trains at stop

    def Signup(self, request, context):
        print("Signup request received")
        n = sensor_pb2.SignupReply()
        train_id = request.train_id
        # check if user exists
        if train_id in self.trains.keys():
            n.success = False
            n.error = "Train already on track."
            print("Duplicate train start request from {}".format(train_id))
        else:    
            self.trains[train_id] = {"status": None, "queue": queue.SimpleQueue()}
            # once user activated, then re-queue undelivered messages
            print("Train {} set on the track".format(train_id))
            n.success = True
        return n    
    
    def Signout(self, request, context):
        n = sensor_pb2.SignupReply()
        train_id = request.train_id
        # if train_id not in self.trains.keys():
        #     n.success = False
        #     n.error = "No existing train found."
        #     print("Nonexistent train leaving request from {}".format(train_id))
        # else:
        del self.trains[train_id]
        print(self.trains)
        print("Train {} left the track.".format(train_id))
        return n
    
    def ResetSensor(self, request, context):
        for train_id in self.trains.keys():
            forward = sensor_pb2.TrainConnectReply()
            forward.train_id = train_id
            forward.alarm = True # alarm
            forward.new_speed = TRAIN_SPEED
            forward.message = "Restarting train to normal speed"
            self.trains[train_id]["queue"].put(forward)
        return sensor_pb2.ResetSensorResponse(success=True,error="None")


    def GetTrainStatus(self, request, context):
        train_id = request.train_id
        if train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {train_id} not found')
        
        train_status = self.trains[train_id]["status"]
        return train_status

    def UpdateTrainStatus(self, request, context):
        train_id = request.train_id
        
        # check if train at stop
        self.train_at_stop = (request.location == STOP_POS % TRACK_LENGTH)

        self.trains[train_id]["status"] = sensor_pb2.TrainStatusResponse(
            train_id=train_id,
            location=request.location,
            speed=request.speed,
        )
        return sensor_pb2.TrainUpdateResponse(success=True)

    def GetOtherTrainStatus(self, request, context):
        other_train_id = request.other_train_id
        if other_train_id not in self.trains:
            return sensor_pb2.TrainStatusResponse(train_id=-1)  # Return "not found" status

        train_status = self.trains[other_train_id]["status"]
        return train_status
    
    # The stream which will be used to send new messages to clients
    # TO DO
    def TrainSensorStream(self, request, context):
        """
        This is a response-stream type call. This means the server can keep sending messages
        Every client opens this connection and waits for server to send new messages
        :param request_iterator:
        :param context:
        :return:
        """
        train_id = request.train_id
        # infinite loop starts for each client
        while True:
            # Check if recipient is active, if they have queued messages
            # if self.trains[train_id]["active"]:
            if self.trains[train_id]["queue"].qsize() > 0: 
                n = self.trains[train_id]["queue"].get(block=False)
                yield n 
    
    def SendSensorMessage(self, request, context):
        id = request.id 
        alarm_bool = request.alarm
        message = request.message

        if alarm_bool: # alarm sensor; someone fell
            # check if any trains are at stop
            if not self.train_at_stop:
                # tell all trains to stop 
                for train_id in self.trains.keys():
                    forward = sensor_pb2.TrainConnectReply()
                    forward.train_id = train_id
                    forward.alarm = alarm_bool
                    forward.new_speed = 0
                    forward.message = message
                    self.trains[train_id]["queue"].put(forward)

            # prompt user to input once person has been rescued??

        else: # warningg sensor; someone crossed the line
            print("Please step away from the tracks.")

        return sensor_pb2.SensorResponse(
            id=id,
            success=True,
            error_message = None
        )
    
    def SensorConnect(self, request, context):
        sensor_id = request.sensor_id
        sensor_type = "Warning"
        if request.alarm:
            sensor_type = "Alarm"
        print(f"Successful connection with {sensor_type} Sensor {sensor_id}")
        return sensor_pb2.SensorConnectResponse(success=True,error="none")


def serve(): 
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    local_ip = socket.gethostbyname(socket.gethostname())
    server.add_insecure_port(f'{local_ip}:50052')
    server.start()
    print('Server API started...')
    server.wait_for_termination()
    
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()