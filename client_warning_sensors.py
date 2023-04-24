import grpc
import random
import time
import threading
import serial
from playsound import playsound

import sensor_pb2
import sensor_pb2_grpc

class WarningSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50052'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.server_stub = sensor_pb2_grpc.ServerStub(self.channel)
        self.device = serial.Serial("/dev/tty.usbmodem1101", 9600)

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
                
                # break
            

if __name__ == '__main__':
    warning_sensor_client = WarningSensorClient(1)
    warning_sensor_thread = threading.Thread(target=warning_sensor_client.run)
    warning_sensor_thread.start()
    warning_sensor_thread.join()
