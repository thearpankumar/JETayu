import serial
"""import serial
import struct

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

while True:
    line = ser.readline()

    #ser.write(b"?\n")

    data = int.from_bytes(line[:-2], byteorder='big', signed=False)

# print data
    print(data)"""

"""
Sabertooth_Serial_motorA = serial.Serial(
    port=device_name1,  # SERIAL PORT on SBC
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS)

Sabertooth_Serial_motorA.read(struct.pack(">B", int(self.data.replace("left"))))
"""

ser = serial.Serial('/dev/ttyUSB0', 9600)  # HC-12 serial port
while True:
    message = ser.readline().decode().strip()
    print("Received message: ", message)
