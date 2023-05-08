import unittest
from unittest import mock
from unittest import mock
from unittest import TestCase
import grpc
import time

import client_alarm_sensors
import serial

import server
import threading

import sys


class TestWarningSensorClient(unittest.TestCase):

    @mock.patch('client_alarm_sensors.input', create=True)
    def test_run(self, mock_input):
        with open("alarm_test_data.txt", "wb") as f:
            f.write("0|1111\n".encode("utf-8"))
            f.write("1|10\n".encode("utf-8"))
            f.write("1|189\n".encode("utf-8"))
            f.write("1|30\n".encode("utf-8"))
        

        server_thread = threading.Thread(target=server.serve, daemon=True)
        server_thread.start()

        mock_input.side_effect = ["2056", "y"]

        alarm_client = client_alarm_sensors.AlarmSensorClient(1, testing=True)
        # nothing happens
        alarm_client.run()
        time.sleep(2)
        # warning
        alarm_client.run()
        time.sleep(8)
        # warning
        alarm_client.run()
        time.sleep(8)
        alarm_client.run()
        # close client
        alarm_client.channel.close()

        time.sleep(2)

    
if __name__ == '__main__':
    unittest.main()

    sys.exit()