import unittest
from unittest import mock
from unittest import mock
from unittest import TestCase
import grpc
import time

import client_warning_sensors
import serial

import server
import threading

import sys


class TestWarningSensorClient(unittest.TestCase):

    @mock.patch('client_warning_sensors.input', create=True)
    def test_run(self, mock_input):
        with open("warning_test_data.txt", "wb") as f:
            f.write("0\n".encode("utf-8"))
            f.write("1\n".encode("utf-8"))
            f.write("1\n".encode("utf-8"))
        
        server_thread = threading.Thread(target=server.serve, daemon=False)
        server_thread.start()

        mock_input.side_effect = ["2056"]
        warning_client = client_warning_sensors.WarningSensorClient(1, testing=True)
        # nothing happens
        warning_client.run()
        time.sleep(1)
        # warning
        warning_client.run()
        time.sleep(8)
        # warning
        warning_client.run()
        # close client
        warning_client.channel.close()

        time.sleep(2)

    
if __name__ == '__main__':
    unittest.main()

    # sys.exit()