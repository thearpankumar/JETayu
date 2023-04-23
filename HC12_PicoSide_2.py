import machine

uart = machine.UART(0, 9600) # UART0 with baud rate 9600
uart.init(9600, bits=8, parity=None, stop=1, rx=1, tx=0) # Initialize UART with specified parameters

while True:
    if uart.any():
        data = uart.read(1) # Read one byte from UART
        print("Received: " + data.decode()) # Decode and print received data