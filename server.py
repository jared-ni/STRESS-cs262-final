import grpc
from concurrent import futures
import time

import train_pb2
import train_pb2_grpc

class Server(train_pb2_grpc.SchedulerServicer):
    def __init__(self):
        self.trains = {}  # Dictionary to store train status
    
    def GetTrainStatus(self, request, context):
        train_id = request.train_id
        if train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {train_id} not found')
        
        train_status = self.trains[train_id]
        return train_status

    def UpdateTrainStatus(self, request, context):
        train_id = request.train_id
        self.trains[train_id] = train_pb2.TrainStatusResponse(
            train_id=train_id,
            location=request.location,
            speed=request.speed,
        )
        return train_pb2.TrainUpdateResponse(success=True)

    def GetOtherTrainStatus(self, request, context):
        other_train_id = request.other_train_id
        if other_train_id not in self.trains:
            return train_pb2.TrainStatusResponse(train_id=-1)  # Return "not found" status

        train_status = self.trains[other_train_id]
        return train_status

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    train_pb2_grpc.add_SchedulerServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Scheduler API started...')
    
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()