"""#nothing to code right now
from machine import I2C, Pin
import time

# MPU9250 address and register definitions
MPU9250_ADDR = 0x68
MPU9250_SMPLRT_DIV = 0x19
MPU9250_CONFIG = 0x1A
MPU9250_GYRO_CONFIG = 0x1B
MPU9250_ACCEL_CONFIG = 0x1C
MPU9250_ACCEL_XOUT_H = 0x3B
MPU9250_PWR_MGMT_1 = 0x6B
MPU9250_WHO_AM_I = 0x75

# AK8963 address and register definitions
AK8963_ADDR = 0x0C
AK8963_WHO_AM_I = 0x00
AK8963_CNTL = 0x0A
AK8963_XOUT_L = 0x03

# Create I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21))

# Function to read a 16-bit value from two 8-bit registers
def read_16bit(reg_h, reg_l):
    val_h = i2c.readfrom_mem(MPU9250_ADDR, reg_h, 1)[0]
    val_l = i2c.readfrom_mem(MPU9250_ADDR, reg_l, 1)[0]
    val = (val_h << 8) | val_l
    return val

# Function to write a byte to a register
def write_byte(reg, val):
    i2c.writeto_mem(MPU9250_ADDR, reg, bytes([val]))

# Initialize MPU9250
write_byte(MPU9250_PWR_MGMT_1, 0x80)  # Reset device
time.sleep(0.1)
write_byte(MPU9250_PWR_MGMT_1, 0x01)  # Auto select clock source
write_byte(MPU9250_SMPLRT_DIV, 0x07)  # Set sample rate to 1kHz
write_byte(MPU9250_CONFIG, 0x00)  # Set gyro to full scale range of +/- 250 degrees/s
write_byte(MPU9250_GYRO_CONFIG, 0x00)  # Set accelerometer to full scale range of +/- 2g
write_byte(MPU9250_ACCEL_CONFIG, 0x00)  # Disable self-test mode
write_byte(MPU9250_PWR_MGMT_1, 0x00)  # Set clock source to PLL with gyroscope reference

# Initialize AK8963
write_byte(MPU9250_PWR_MGMT_1, 0x10)  # Enable I2C master mode
write_byte(MPU9250_I2C_MST_CTRL, 0x0D)  # Set I2C bus speed to 400kHz
write_byte(MPU9250_I2C_SLV0_ADDR, AK8963_ADDR | 0x80)  # Set AK8963 address and read mode bit
write_byte(MPU9250_I2C_SLV0_REG, AK8963_WHO_AM_I)  # Set AK8963 register to read WHO_AM_I
write_byte(MPU9250_I2C_SLV0_CTRL, 0x81)  # Enable I2C slave 0 and set length to read 1 byte
time.sleep(0.1)
ak8963_id = i2c.readfrom_mem(MPU9250_ADDR, MPU9250_EXT_SENS_DATA_00)"""
import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
import socket

# Set country to avoid possible errors
rp2.country('IN')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# If you need to disable powersaving mode
# wlan.config(pm = 0xa11140)

# See the MAC address in the wireless chip OTP
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# Other things to query
# print(wlan.config('channel'))
# print(wlan.config('essid'))
# print(wlan.config('txpower'))

# Load login data from different file for safety reasons
ssid = "SSID" 
password = "passworD"

wlan.connect(ssid, password)

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)

# Define blinking function for onboard LED to indicate error codes    
def blink_onboard_led(num_blinks):
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(num_blinks):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)
    
# Handle connection error
# Error meanings
# 0  Link Down
# 1  Link Join
# 2  Link NoIp
# 3  Link Up
# -1 Link Fail
# -2 Link NoNet
# -3 Link BadAuth

wlan_status = wlan.status()
blink_onboard_led(wlan_status)

if wlan_status != 3:
    raise RuntimeError('Wi-Fi connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    
# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)
led = machine.Pin('LED', machine.Pin.OUT)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        r = cl.recv(1024)
        # print(r)
        
        r = str(r)
        led_on = r.find('?led=on')
        led_off = r.find('?led=off')
        print('led_on = ', led_on)
        print('led_off = ', led_off)
        if led_on > -1:
            print('LED ON')
            led.value(1)
            
        if led_off > -1:
            print('LED OFF')
            led.value(0)
            2
        response = get_html('index.html')
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('Connection closed')

# Make GET request
#request = requests.get('http://www.google.com')
#print(request.content)
#request.close()