import grpc
import random
import time
import threading
import serial
from playsound import playsound

import sensor_pb2
import sensor_pb2_grpc

class WarningSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.server_stub = sensor_pb2_grpc.ServerStub(self.channel)
        self.device = serial.Serial("/dev/tty.usbmodem1101", 9600)

    def send_message(self, sensor_id, alarm, message):
        request = sensor_pb2.SensorMessageRequest(id = sensor_id, alarm = alarm, message = message)
        response = self.server_stub.SendSensorMessage(request)
        return response


    def run(self):
        # print(f'Sending data')
        self.send_message(self.sensor_id, "REGISTER")
        while True:
            time.sleep(0.1)
            ultrasonic = self.device.readline().decode('utf-8').rstrip()
            if int(ultrasonic) <= 50:
                self.send_message(self.sensor_id, "WARNING")
                playsound('/untitled.wav')
                break
            

if __name__ == '__main__':
    warning_sensor_client = WarningSensorClient(1)
    warning_sensor_thread = threading.Thread(target=warning_sensor_client.run)
    warning_sensor_thread.start()
    warning_sensor_thread.join()
