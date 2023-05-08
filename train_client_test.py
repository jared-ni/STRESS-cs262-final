import unittest
from unittest import mock
from unittest import mock
from unittest import TestCase
import grpc
import time

import train_client
import serial

import server
import threading

import sys

class TestTrainClient(unittest.TestCase):

    @mock.patch('train_client.input', create=True)
    def test_signup(self, mock_input):     
        mock_input.side_effect = ["2056"]  
        server_thread = threading.Thread(target=server.serve, daemon=True)
        server_thread.start()
       
        self.train_client_test = train_client.TrainClient()
        self.train_client_test.train_id = 3

        time.sleep(5)

        reply = self.train_client_test.signup(self.train_client_test.train_id)
        self.train_client_test.thread()
        self.assertEqual(reply.success, True)


    @mock.patch('train_client.input', create=True)
    def test_update_and_get_status(self, mock_input):

        server_thread = threading.Thread(target=server.serve, daemon=True)
        server_thread.start()
        time.sleep(2)
        mock_input.side_effect = ["2056"]
    

        self.train_client_test = train_client.TrainClient()
        self.train_client_test.train_id = 1

        reply = self.train_client_test.signup(self.train_client_test.train_id)
        self.train_client_test.thread()    
        while not self.train_client_test.is_safe_to_instantiate():
            time.sleep(1)
        train_status = self.train_client_test.update_status()
        self.assertEqual(train_status, True)
        train_status = self.train_client_test.get_status()
        self.assertEqual(train_status.train_id, 1)

    @mock.patch('train_client.input', create=True)
    def test_get_other_train_status(self, mock_input):

        server_thread = threading.Thread(target=server.serve, daemon=True)
        server_thread.start()
        time.sleep(2)
        mock_input.side_effect = ["2056"]

    
        self.train_client_test = train_client.TrainClient()
        self.train_client_test.train_id = 1

        reply = self.train_client_test.signup(self.train_client_test.train_id)
        self.train_client_test.thread()    

        # get_other_train_status is called by and is only used for is_safe_to_instantiate
        status = self.train_client_test.is_safe_to_instantiate()
        self.assertEqual(status, True)
    
if __name__ == '__main__':
    unittest.main()

    sys.exit()