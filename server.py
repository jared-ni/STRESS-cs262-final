import grpc
from concurrent import futures
import time
import queue
import random

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

gary = "10.250.145.248"
jessica = "10.250.135.58"
ports = {
    2056: jessica, 
    3056: gary,
    4056: jessica
}

class Server(sensor_pb2_grpc.ServerServicer):
    def __init__(self, port):
        self.trains = {}  # Dictionary to store train status
        self.train_at_stop = False # updates if any trains at stop

        # new
        self.port = port 
        self.is_master = False
        self.master = None
        self.conns = {} # dict of all connections to other servers, key (port) -> value (connection)
        self.channels = {}

    # new 
    def is_master_query(self,port):
        n = sensor_pb2.IsMasterRequest()
        reply = self.conns[port].IsMasterQuery(n)
        return reply 
    
    def IsMasterQuery(self, request: sensor_pb2.IsMasterRequest, context):
        n = sensor_pb2.IsMasterReply()
        n.master = self.is_master
        return n

    
    def test_server_activity(self,channel): # test if a given server is active
        TIMEOUT_SEC = random.randint(1,3) # each server can timeout differently
        try: 
            grpc.channel_ready_future(channel).result(timeout=TIMEOUT_SEC) 
            return True 
        except grpc.FutureTimeoutError: 
            return False
        
    def add_connect(self, port):
        # "client" server tells "server" server to connect back
        n = sensor_pb2.AddConnectRequest()
        n.requester_port = self.port
        n.replier_port = port 
        reply = self.conns[port].AddConnect(n)
        return reply
    
    def AddConnect(self, request: sensor_pb2.AddConnectRequest, context):
        # "server" server receives request to connect back
        port = request.requester_port
        print("Receive connect request from {}".format(port))
        self.channels[port] = grpc.insecure_channel(ports[port] + ':' + str(port))
        self.conns[port] = sensor_pb2_grpc.ChatServerStub(self.channels[port])
        print("Connection successful")
        n = sensor_pb2.AddConnectReply()
        n.success = True
        n.error = "Connection back to client-server failed"
        return n
    
    def connect(self):
        for i in list(ports.keys()): 
            if i != self.port:  # all other possible servers except self
                self.channels[i] = grpc.insecure_channel(ports[i] + ':' + str(i))
                if self.test_server_activity(self.channels[i]): # check if active
                    print("Port {} is active".format(i))
                    self.conns[i] = sensor_pb2_grpc.ChatServerStub(self.channels[i]) # add connection
                    self.add_connect(i)
                else: # delete inactive channel from dict
                    del self.channels[i]
        master_found = False
        for port in self.conns:
            reply = self.is_master_query(port)
            if reply.master:
                master_found = True
                self.master = port
                print("Master found at port {}".format(port))
                break
        if not master_found:
            self.is_master = True # for now just make self master
            print("No master found; I am the master")

    def disconnect(self, target_port):
        # "client" server tells "server" server to disconnect
        n = sensor_pb2.DisconnectRequest()
        n.requester_port = self.port
        n.replier_port = target_port 
        n.is_master = self.is_master
        reply = self.conns[target_port].Disconnect(n)
        if reply.success:
            print("Port {} successfully disconnected".format(target_port))
            del self.conns[target_port] # remove from active conns
            self.channels[target_port].close() # close channel
            del self.channels[target_port]
        else:
            print(reply.error)
        return reply   

    def Disconnect(self, request: sensor_pb2.DisconnectRequest, context):
        # "server" server receives request to disconnect
        port = request.requester_port
        print("Received discconnect request from {}".format(port))
        del self.conns[port] # remove from active conns
        self.channels[port].close() # close channel
        del self.channels[port]
        print("Disconnect successful")
        n = sensor_pb2.DisconnectReply()
        n.success = True
        n.error = "Disconnect back to client-server failed"
        if request.is_master: # disconnected server was the master
            self.find_new_master()
        return n

    def disconnect_all(self):
        # server tells all connected servers to shut down conns and channels
        replies = []
        print("Connections:",list(self.conns.keys()))
        for port in list(self.conns.keys()):
            print("Disconnecting from {}".format(port))
            # self.disconnect(port)
            reply = self.disconnect(port)
            replies.append(reply)
        return replies

    def find_new_master(self):
        print("Finding new master")
        active_ports = list(self.conns.keys()) + [self.port]
        active_ports.sort()
        print("Active ports:", active_ports)
        new_master = active_ports[0]
        self.master = new_master
        if new_master == self.port:
            self.is_master = True
            print("I am now the master")
        else:
            print("Port {} is the new master".format(new_master))
        

    # old
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
    port = int(input("Input port number from one of [2056,3056,4056]: "))

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    train_server = Server(port) # new
    
    try: 
        sensor_pb2_grpc.add_ServerServicer_to_server(train_server, server)
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
    except:
        train_server.disconnect_all() # new


if __name__ == '__main__':
    serve()