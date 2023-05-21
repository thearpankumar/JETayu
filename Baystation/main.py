import machine
import utime

import threading
tx_pin = machine.Pin(4)  # Pin number for TX on Raspberry Pi Pico
rx_pin = machine.Pin(5)  # Pin number for RX on Raspberry Pi Pico

uart = machine.UART(1, baudrate=9600, tx=tx_pin, rx=rx_pin)  # Initialize UART with custom TX and RX pins and baudrate 9600
uart.init(9600, bits=8, parity=None, stop=1)

def input_thread():
    while True:
        user_input = input("> ")

def send_thread():
    while True:
        #data =  user_input # Data to send
        data = bytes(user_input, 'utf-8')
        uart.write(data)  # Send data over UART
        utime.sleep(1)  # Delay for 1 second

        if uart.any():
            data = uart.read(1)
            if data is not None:
                received_byte = int.from_bytes(data, 'big')
                print("Received byte: {}".format(received_byte))

"""while True:
    data = 30  # Data to send
    data = bytes(" ", 'utf-8')
    uart.write(data)  # Send data over UART
    utime.sleep(1)  # Delay for 1 second

    if uart.any():
        data = uart.read(1)
        if data is not None:
            received_byte = int.from_bytes(data, 'big')
            print("Received byte: {}".format(received_byte))"""

input_thread = threading.Thread(target=input_thread)
send_thread = threading.Thread(target=send_thread)

input_thread.start()
send_thread.start()


    