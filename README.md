# Stational T-stop Railing Emergency Sirening System
Jessica Chen, Bryan Han, Jared Ni, Gary Wu

## Software Usage and Setup:

Users can instantiate up to three servers, three train clients, and an uncapped number of sensor clients. 

### For Server:

Run `python3 -m server.py` in base directory. You will be prompted to enter a port number; follow instructions to select a port. If the port is already in use, an error message will pop up and you will get the chance to re-enter.

If successful, you'll see a `Server API started...` This will allow the server to start listening to new clients that join and their commands. As clients join and make requests, important updates will be printed to the server command line.

### For Train Client:

Run `python3 -m train_client.py` in base directory. Follow instructions to enter a train ID of 1, 2, or 3; if a duplicate ID is entered, you can re-enter another ID number. If successful, trains will wait for all other trains to be at a safe minimum distance away to instantiate at the train stop. 

### For Warning Sensor Client:

Run `python3 -m client_warning_sensors.py` in base directory.

### For Alarm Sensor Client:

Run `python3 -m client_alarm_sensors.py` in base directory.

### Note IP Addresses

At the moment, IP addresses are hardcoded. The source code can be edited so that the `servers` dictionary in `server.py` accurately reflects the machines used on a given run.

## Helpful Commands
`python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. sensor.proto`
