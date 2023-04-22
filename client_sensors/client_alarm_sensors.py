import grpc
import random
import time
import threading
import serial

import sensor_pb2
import sensor_pb2_grpc

class AlarmSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.alarm_sensor_stub = sensor_pb2_grpc.AlarmSensorStub(self.channel)
        self.device = serial.Serial("/dev/tty.usbmodem1101", 9600)

    def send_message(self, sensor_id, message):
        return sensor_pb2.MessageRequest(id = sensor_id, message = message)

    def run(self):
        # print(f'Sending data')
        while True:
            time.sleep(0.1)
            line = self.device.readline().decode('utf-8').rstrip()
            print(line); line = line.split("|"); 
            ultrasonic = line[0]; pir = line[1]
            if int(ultrasonic) <= 50 and int(pir) == 1:
                self.send_message(self.sensor_id, "FIRE THE ALARMS") 
                break     
            

if __name__ == '__main__':
    alarm_sensor_client = AlarmSensorClient(1)
    alarm_sensor_thread = threading.Thread(target=alarm_sensor_client.run)
    alarm_sensor_thread.start()
    alarm_sensor_thread.join()
