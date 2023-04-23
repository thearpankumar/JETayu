"""
import serial
import struct

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

while True:
    line = ser.readline()#.decode("utf-8")
    #print(line)

    #ser.write(b"?\n")

    data = int.from_bytes(line[:-2], byteorder='big', signed=False)

# print data
    print(data)
"""
import machine
import time

# Specify the USB port for the HC-12 module
uart = machine.UART(0, 9600) # Use UART 0 with baud rate 9600
uart.init(9600, bits=8, parity=None, stop=1) # Initialize UART with 8 data bits, no parity, and 1 stop bit

while True:
    if uart.any():
        data = uart.read().decode() # Read and decode the received data
        print("Received:", data)
        
    time.sleep(1) # Delay for 1 second