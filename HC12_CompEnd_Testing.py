import serial
import time

ser = serial.Serial('/dev/ttyUSB1', 9600) # HC-12 serial port
while True:
    #message = input("Enter message to send: ")
    message = 'i'
    ser.write(message.encode())
    time.sleep(1)
    print(message)

"""
Sabertooth_Serial_motorA = serial.Serial(
    port=device_name1,  # SERIAL PORT on SBC
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

Sabertooth_Serial_motorA.read(struct.pack(">B", int(self.data.replace("left"))))
"""
