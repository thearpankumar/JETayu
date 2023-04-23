import machine
import time

uart = machine.UART(0, 9600) # Use UART 0 with baud rate 9600
uart.init(9600, bits=8, parity=None, stop=1) # Initialize UART with 8 data bits, no parity, and 1 stop bit

while True:
    if uart.any():
        data = uart.read(1).decode() # Read and decode the received data
        print("Received:", data)
        
    time.sleep(1) # Delay for 1 second
"""
    message = "Hello, world!" # The string to send
        uart.write(message.encode()) # Convert the string to bytes and send over UART
        print("Sent:", message)
"""