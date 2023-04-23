import grpc
from concurrent import futures
import time

import sys
sys.path.append("client_sensors")
import sensor_pb2
import sensor_pb2_grpc

MIN_SAFE_DIST = 10
TRACK_LENGTH = 30
STOP_POS = 30
TRAIN_SPEED = 1
UPDATE_RATE = 3

class Server(sensor_pb2_grpc.ServerServicer):
    def __init__(self):
        self.trains = {}  # Dictionary to store train status
        self.train_at_stop = False # updates if any trains at stop
    
    def GetTrainStatus(self, request, context):
        train_id = request.train_id
        if train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {train_id} not found')
        
        train_status = self.trains["status"][train_id]
        return train_status

    def UpdateTrainStatus(self, request, context):
        train_id = request.train_id
        
        # check if train at stop
        self.train_at_stop = (request.location == STOP_POS % TRACK_LENGTH)

        self.trains["status"][train_id] = sensor_pb2.TrainStatusResponse(
            train_id=train_id,
            location=request.location,
            speed=request.speed,
        )
        return sensor_pb2.TrainUpdateResponse(success=True)

    def GetOtherTrainStatus(self, request, context):
        other_train_id = request.other_train_id
        if other_train_id not in self.trains:
            return sensor_pb2.TrainStatusResponse(train_id=-1)  # Return "not found" status

        train_status = self.trains["status"][other_train_id]
        return train_status
    
    # The stream which will be used to send new messages to clients
    # TO DO
    def AlarmStream(self, request: sensor_pb2.TrainConnectRequest, context):
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
                    forward = sensor_pb2.ConnectReply()
                    forward.train_id = train_id
                    forward.alarm = alarm_bool
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
    
 

# class Server(sensor_pb2_grpc.AlarmSensorServicer):
#     def __init__(self):
#         self.sensors = {}

#     def SendData(self, request, context):
#         if request.message == "REGISTER":
#             self.sensors[request.id] = 0
#         elif request.message == "FIRE THE ALARMS":
#             self.sensors[request.id] = 1
#             counter = 0
#             for key, item in self.sensors.item():
#                 if item == 1: counter += 1
#             if counter >= 1:
#                 pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensor_pb2_grpc.add_ServerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server API started...')
    
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()