import grpc
import random
import time
import threading
import serial
from playsound import playsound

import train_pb2
import train_pb2_grpc

class AlarmSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.alarm_sensor_stub = train_pb2_grpc.AlarmSensorStub(self.channel)
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
            line = self.device.readline().decode('utf-8').rstrip()
            print(line); line = line.split("|"); 
            ultrasonic = line[0]; pir = line[1]
            if int(ultrasonic) <= 50 and int(pir) == 1:
                self.send_message(self.sensor_id, "FIRE THE ALARMS") 
                playsound('someonefellin.wav')
                break     
            

if __name__ == '__main__':
    alarm_id = int(input("Enter sensor ID (1, 2, or 3) to connect a sensor or 0 to exit: "))

    if alarm_id == 0:
        print("Exiting.")
    elif alarm_id in [1, 2, 3]:
        alarm_sensor_client = AlarmSensorClient(alarm_id)
        alarm_sensor_thread = threading.Thread(target=alarm_sensor_client.run)
        alarm_sensor_thread.start()
        alarm_sensor_thread.join()
    else:
        print("Invalid train ID. Please enter 1, 2, or 3.")