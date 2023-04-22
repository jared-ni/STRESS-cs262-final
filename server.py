import grpc
from concurrent import futures
import time

import train_pb2
import train_pb2_grpc

class SchedulerImpl(train_pb2_grpc.SchedulerServicer):
    def __init__(self):
        self.trains = {}  # Dictionary to store train status

    def GetTrainStatus(self, request, context):
        train_id = request.train_id
        if train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {train_id} not found')
        
        train_status = self.trains[train_id]
        return train_pb2.TrainStatusResponse(
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

        return train_pb2.TrainUpdateResponse(success=True)

 
    def GetOtherTrainStatus(self, request, context):
        other_train_id = request.other_train_id
        if other_train_id not in self.trains:
            context.abort(grpc.StatusCode.NOT_FOUND, f'Train {other_train_id} not found')

        train_status = self.trains[other_train_id]
        return train_pb2.TrainStatusResponse(
            train_id=other_train_id,
            location=train_status.location,
            speed=train_status.speed,
            distance_to_stop=train_status.distance_to_stop
        )



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    train_pb2_grpc.add_SchedulerServicer_to_server(SchedulerImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Scheduler API started...')
    
    try:
        while True:
            time.sleep(60 * 60 * 24)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    train_clients = {}
    train_threads = {}

    while True:
        train_id = int(input("Enter train ID (1, 2, or 3) to instantiate a train or 0 to exit: "))
        if train_id == 0:
            break
        elif train_id in [1, 2, 3]:
            if train_id not in train_clients:
                train_client = TrainClient(train_id)
                train_clients[train_id] = train_client

                train_thread = threading.Thread(target=train_client.run)
                train_threads[train_id] = train_thread
                train_thread.start()
            else:
                print(f'Train {train_id} is already instantiated.')
        else:
            print("Invalid train ID. Please enter 1, 2, or 3.")

    # Wait for all train threads to finish
    for train_thread in train_threads.values():
        train_thread.join()
