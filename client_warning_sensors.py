import grpc
import random
import time
import threading
import serial
from playsound import playsound

import sensor_pb2
import sensor_pb2_grpc
import socket

class WarningSensorClient:
    def __init__(self, sensor_id, 
                 server_address=f'{socket.gethostbyname(socket.gethostname())}:50052', testing=False):
        server_ip = input("Are you running server on localhost? (y/n) ")
        while True:
            if server_ip == "y":
                break
            elif server_ip == "n":
                ip_addr = input("Enter server ip address: ")
                server_address = ip_addr + ":50052"
                break
            else:
                server_ip = input("Are you running server on localhost? (y/n)")

        print(f'Connecting to server at {server_address}...')
        self.testing = testing
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.server_stub = sensor_pb2_grpc.ServerStub(self.channel)
        if not testing:
            self.device = serial.Serial("/dev/tty.usbmodem2101", 9600)
        else:
            self.device = open("warning_test_data.txt", "rb")

        n = sensor_pb2.SensorConnectRequest(sensor_id=sensor_id,alarm=False)
        reply = self.server_stub.SensorConnect(n)

    def send_message(self, sensor_id, alarm, message):
        request = sensor_pb2.SensorMessageRequest(id = sensor_id, alarm = alarm, message = message)
        response = self.server_stub.SendSensorMessage(request)
        return response


    def run(self):
        print(f'Sending data')
        reading = False
        # self.send_message(self.sensor_id, "REGISTER")
        while True:
            time.sleep(0.1)
            pir = int(self.device.readline().decode('utf-8').rstrip())
            print(pir)
            if pir == 1 and not reading:
                reading = True
                self.send_message(self.sensor_id, True, "WARNING")
                my_thread = threading.Thread(target=playsound, args = ('warning.m4a',))
                my_thread.start()
            elif pir == 0 and reading:
                reading = False
                
            if self.testing:
                break
            

if __name__ == '__main__':
    warning_sensor_client = WarningSensorClient(1)
    warning_sensor_thread = threading.Thread(target=warning_sensor_client.run)
    warning_sensor_thread.start()
    warning_sensor_thread.join()
