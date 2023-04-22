import grpc
import random
import time
import threading
import serial

import alarm_sensor_pb2
import alarm_sensor_pb2_grpc

class AlarmSensorClient:
    def __init__(self, sensor_id, server_address='localhost:50051'):
        self.sensor_id = sensor_id
        self.channel = grpc.insecure_channel(server_address)
        self.alarm_sensor_stub = alarm_sensor_pb2_grpc.AlarmSensorStub(self.channel)
        self.devices = [serial.Serial("/dev/tty.usbmodem101", 9600)]

    def send_data(self, sensor_id, pir_data, ultrasonic_data):
        request = alarm_sensor_pb2_grpc.Data(id=sensor_id, pir_data=pir_data, ultrasonic_data=ultrasonic_data)
        response = self.alarm_sensor_stub.SendData(request)
        return response

    def run(self):
        # print(f'Sending data')

        while True:
            for device in self.devices:
                line = device.readline().decode('utf-8').rstrip()
                self.send_data(line)

if __name__ == '__main__':
    id = 1
    alarm_sensor_client = AlarmSensorClient(id)
    
    alarm_sensor_thread = threading.Thread(target=alarm_sensor_client.run)
    alarm_sensor_thread.start()
    alarm_sensor_thread.join()
