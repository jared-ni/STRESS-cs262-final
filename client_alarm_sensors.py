import grpc
import random
import time
import threading
import serial
from playsound import playsound

import sensor_pb2
import sensor_pb2_grpc

class AlarmSensorClient:
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
        print(f'Sending data')
        # self.send_message(self.sensor_id, "REGISTER")
        reading = False
        while True:
            time.sleep(0.1)
            line = self.device.readline().decode('utf-8').rstrip()
            print(line); line = line.split("|"); 
            pir, ultrasonic = int(line[0]), int(line[1])
            if pir == 1 and ultrasonic <= 100 and not reading:
                reading = True
                self.send_message(self.sensor_id, True, "FIRE THE ALARMS") 
                playsound('someonefellin.wav')
            elif int(pir) == 0 and reading:
                reading = False
                n = sensor_pb2.ResetSensorRequest()
                reply = self.server_stub.ResetSensor(n)


if __name__ == '__main__':
    alarm_sensor_client = AlarmSensorClient(1)
    alarm_sensor_thread = threading.Thread(target=alarm_sensor_client.run)
    alarm_sensor_thread.start()
    alarm_sensor_thread.join()
