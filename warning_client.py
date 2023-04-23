import grpc
import random
import time
import threading
import serial
from playsound import playsound

import train_pb2
import train_pb2_grpc

class WarningSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.warning_sensor_stub = train_pb2_grpc.WarningSensorStub(self.channel)
        self.device = serial.Serial("/dev/tty.usbmodem1101", 9600)

    def send_message(self, sensor_id, message):
        return train_pb2.SensorMessageRequest(
            id = sensor_id, 
            alarm = True,
            message = message
        )

    def run(self):
        # print(f'Sending data')
        while True:
            time.sleep(0.1)
            ultrasonic = self.device.readline().decode('utf-8').rstrip()
            if int(ultrasonic) <= 50:
                self.send_message(self.sensor_id, "WARNING")
                playsound('/untitled.wav')
                break
            

if __name__ == '__main__':
    warning_id = int(input("Enter sensor ID (1, 2, or 3) to connect a sensor or 0 to exit: "))

    if warning_id == 0:
        print("Exiting.")
    elif warning_id in [1, 2, 3]:
        warning_sensor_client = WarningSensorClient(warning_id)
        warning_sensor_client = threading.Thread(target=warning_sensor_client.run)
        warning_sensor_client.start()
        warning_sensor_client.join()
    else:
        print("Invalid train ID. Please enter 1, 2, or 3.")
