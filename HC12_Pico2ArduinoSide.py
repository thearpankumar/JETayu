import machine
import time

uart = machine.UART(0, 9600) # UART0 with baud rate 9600

tx_pin = machine.Pin(0) # Pin for TX
rx_pin = machine.Pin(1) # Pin for RX
uart.init(9600, bits=8, parity=None, stop=1) # Initialize UART with specified parameters

while True:
    if uart.any():
        data = uart.read().decode('utf-8') # Read one byte from UART
        print("Received: " + data) # Decode and print received dataa
