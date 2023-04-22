import grpc
import random
import time
import threading

import train_pb2
import train_pb2_grpc

class TrainClient:
    def __init__(self, train_id, server_address='localhost:50051'):
        self.train_id = train_id
        self.channel = grpc.insecure_channel(server_address)
        self.scheduler_stub = train_pb2_grpc.SchedulerStub(self.channel)

    def get_status(self):
        request = train_pb2.TrainStatusRequest(train_id=self.train_id)
        response = self.scheduler_stub.GetTrainStatus(request)
        return response

    def update_status(self, location, speed):
        request = train_pb2.TrainUpdateRequest(train_id=self.train_id, location=location, speed=speed)
        response = self.scheduler_stub.UpdateTrainStatus(request)
        return response.success
    
    
    def is_safe_to_instantiate(self):
        other_train_ids = [1, 2, 3]
        other_train_ids.remove(self.train_id)

        train_statuses = []
        for other_train_id in other_train_ids:
            train_status = self.get_other_train_status(other_train_id)
            if train_status.train_id != -1:  # If the train is instantiated
                train_statuses.append(train_status)

        if not train_statuses:
            return True

        for train_status in train_statuses:
            distance_to_train = train_status.distance_to_stop  # Assuming the train will start at the stop
            time_to_collision = distance_to_train / train_status.speed
            if time_to_collision >= 10:
                return True

        return False
    
    def get_other_train_status(self, other_train_id):
        request = train_pb2.OtherTrainStatusRequest(requesting_train_id=self.train_id, other_train_id=other_train_id)
        response = self.scheduler_stub.GetOtherTrainStatus(request)
        return response


    def run(self):
        print(f'Train {self.train_id} waiting for instantiation...')

        while not self.is_safe_to_instantiate():
            time.sleep(1)

        print(f'Train {self.train_id} instantiated...')

        print(f'Train {self.train_id} started...')

        while True:
            # Simulate train movement and speed updates
            location = random.uniform(0, 100)  # Replace with actual location calculation
            speed = random.uniform(40, 100)    # Replace with actual speed calculation

            # Update train status in Scheduler API
            update_success = self.update_status(location, speed)
            if not update_success:
                print(f'Error updating train {self.train_id} status.')

            # Get train status from Scheduler API
            train_status = self.get_status()
            print(f'Train {self.train_id} status: location={train_status.location}, speed={train_status.speed}, distance_to_stop={train_status.distance_to_stop}')

            time.sleep(5)  # Wait for some time before next update

      
            # Get the status of another train and check for potential collision
            other_train_id = 2 if self.train_id == 1 else 1
            other_train_status = self.get_other_train_status(other_train_id)
            distance_between_trains = other_train_status.location - train_status.location

            if distance_between_trains > 0 and distance_between_trains / (train_status.speed - other_train_status.speed) < 2 * 60:
                # Slow down to match the speed of the other train
                speed = other_train_status.speed
                print(f'Train {self.train_id} slowing down to avoid collision.')

            time.sleep(5)  # Wait for some time before next update


if __name__ == '__main__':
    train_id = 1
    train_client = TrainClient(train_id)
    
    train_thread = threading.Thread(target=train_client.run)
    train_thread.start()
    train_thread.join()
