import machine
import utime

tx_pin = machine.Pin(4)  # Pin number for TX on Raspberry Pi Pico
rx_pin = machine.Pin(5)  # Pin number for RX on Raspberry Pi Pico

uart = machine.UART(1, baudrate=9600, tx=tx_pin, rx=rx_pin)  # Initialize UART with custom TX and RX pins and baudrate 9600
uart.init(9600, bits=8, parity=None, stop=1)

while True:
    if uart.any():
        data = uart.read(1)
        if data is not None:
            received_byte = int.from_bytes(data, 'big')
            print("Received byte: {}".format(received_byte))
    