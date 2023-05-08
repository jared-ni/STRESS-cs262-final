import grpc
import random
import time
import threading
import serial
from playsound import playsound

import sensor_pb2
import sensor_pb2_grpc
import socket


gary = socket.gethostbyname(socket.gethostname())
jessica = socket.gethostbyname(socket.gethostname())
servers = {
    2056: jessica, #jessica
    3056: gary,
    4056: jessica
}
class WarningSensorClient:
    def __init__(self, sensor_id, 
                 server_address=f'{socket.gethostbyname(socket.gethostname())}:50052', testing=False):
        # server_ip = input("Are you running server on localhost? (y/n) ")
        # while True:
        #     if server_ip == "y":
        #         break
        #     elif server_ip == "n":
        #         ip_addr = input("Enter server ip address: ")
        #         server_address = ip_addr + ":50052"
        #         break
        #     else:
        #         server_ip = input("Are you running server on localhost? (y/n)")

        # print(f'Connecting to server at {server_address}...')
        self.testing = testing
        self.sensor_id = sensor_id
        # self.channel = grpc.insecure_channel(server_address)
        # self.server_stub = sensor_pb2_grpc.ServerStub(self.channel)
        # if not testing:
        #     self.device = serial.Serial("/dev/tty.usbmodem2101", 9600)
        # else:
        #     self.device = open("warning_test_data.txt", "rb")

        # n = sensor_pb2.SensorConnectRequest(sensor_id=sensor_id,alarm=False)
        # reply = self.server_stub.SensorConnect(n)

        self.channel = None
        self.server_stub = None # self.conn
        self.master = None

        # connect to each port to find master server 
        for port in list(servers.keys()):
            self.channel = grpc.insecure_channel(servers[port] + ':' + str(port))
            if self.test_server_activity(self.channel):
                print("Server at port {} is active".format(port))
                self.server_stub = sensor_pb2_grpc.ServerStub(self.channel) # add connection
                reply = self.is_master_query(port)
                if reply.master: # connection is master
                    self.master = port
                    print("Master found at port {}".format(port))

                    # from new
                    if not testing:
                        self.device = serial.Serial("/dev/tty.usbmodem1101", 9600)
                    else:
                        self.device = open("alarm_test_data.txt", "rb")

                    n = sensor_pb2.SensorConnectRequest(sensor_id=sensor_id, alarm=False)
                    reply = self.server_stub.SensorConnect(n)
                    break
                else: 
                    self.server_stub = None # break connection
                    self.channel = None
        if self.server_stub is None:
            print("Error: no connection found.")
        if self.master is None: # no master found
            print("Error: no master found.")


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

    def test_server_activity(self,channel): # test if a given server is active
        TIMEOUT_SEC = random.randint(1,3) # each server can timeout differently
        try: 
            grpc.channel_ready_future(channel).result(timeout=TIMEOUT_SEC) 
            return True 
        except grpc.FutureTimeoutError: 
            return False
        
    def is_master_query(self,port):
        n = sensor_pb2.IsMasterRequest()
        reply = self.conn.IsMasterQuery(n)
        return reply 
    
    def reconnect_server(self):
        # given disconnected server, connect to another master
        print("Reconnecting server")
        failed_port = self.master
        self.channel = None 
        self.master = None 
        self.server_stub = None

        for port in list(servers.keys()):
            if port != failed_port: # not the one that just disconnected
                self.channel = grpc.insecure_channel(servers[port] + ':' + str(port))
                if self.test_server_activity(self.channel):
                    print("Server at port {} is active".format(port))
                    self.conn = sensor_pb2_grpc.ServerStub(self.channel) # add connection
                    reply = self.is_master_query(port)
                    if reply.master: # connection is master
                        self.master = port
                        print("Master found at port {}".format(port))

                        # from new
                        self.device = open("alarm_test_data.txt", "rb")

                        n = sensor_pb2.SensorConnectRequest(sensor_id=self.sensor_id, alarm=True)
                        reply = self.server_stub.SensorConnect(n)
                        break
                    else: 
                        self.conn = None # break connection
                        self.channel = None
        if self.conn is None:
            print("Error: no connection found.")
        if self.master is None: # no master found
            print("Error: no master found.")
            

if __name__ == '__main__':
    warning_sensor_client = WarningSensorClient(1)
    while True:
        try:   
            warning_sensor_thread = threading.Thread(target=warning_sensor_client.run)
            warning_sensor_thread.start()
            warning_sensor_thread.join()
        except:
            warning_sensor_client.channel.close() # important
            time.sleep(1) # servers need time to figure out who is master
            warning_sensor_client.reconnect_server()
