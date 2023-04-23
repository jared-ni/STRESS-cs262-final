import serial

devices = [serial.Serial("/dev/tty.usbmodem101", 9600)]
 
while True:
    for device in devices:
        line = device.readline().decode('utf-8').rstrip()
        print(line)