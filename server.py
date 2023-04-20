import grpc
from concurrent import futures
import time

import scheduler_pb2
import scheduler_pb2_grpc

class SchedulerImpl(scheduler_pb2_grpc.SchedulerServicer):
    def __init__(self):
        self.trains = {}  # Dictionary to store train status

    def GetTrainStatus(self, request, context):
        train_id = request.train_id
        if train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {train_id} not found')
        
        train_status = self.trains[train_id]
        return scheduler_pb2.TrainStatusResponse(
            train_id=train_id,
            location=train_status.location,
            speed=train_status.speed,
            distance_to_stop=train_status.distance_to_stop
        )

    def UpdateTrainStatus(self, request, context):
        train_id = request.train_id
        self.trains[train_id] = TrainStatus(
            location=request.location,
            speed=request.speed
        )
        # Check for trains too close to each other and send slow down signals
        # ...

        return scheduler_pb2.TrainUpdateResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    scheduler_pb2_grpc.add_SchedulerServicer_to_server(SchedulerImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Scheduler API started...')
    
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name
