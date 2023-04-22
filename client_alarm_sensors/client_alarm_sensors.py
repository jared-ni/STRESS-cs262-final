import grpc
import random
import time
import threading

import alarm_sensor_pb2
import alarm_sensor_pb2_grpc

class AlarmSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.scheduler_stub = alarm_sensor_pb2_grpc.AlarmsensorStub(self.channel)

    def send_data(self):
        request = alarm_sensor_pb2_grpc.Data(train_id=self.train_id)
        response = self.scheduler_stub.GetTrainStatus(request)
        return response

    def update_status(self, location, speed):
        request = alarm_sensor_pb2_grpc.TrainUpdateRequest(train_id=self.train_id, location=location, speed=speed)
        response = self.scheduler_stub.UpdateTrainStatus(request)
        return response.success

    def run(self):
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

if __name__ == '__main__':
    train_id = 1
    train_client = TrainClient(train_id)
    
    train_thread = threading.Thread(target=train_client.run)
    train_thread.start()
    train_thread.join()
