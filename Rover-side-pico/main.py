from machine import *
import utime
from time import sleep_us, sleep
from imu import MPU6050
#from time import sleep
#from machine import Pin, I2C
import BME280

sda=machine.Pin(16)
scl=machine.Pin(17)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

ECHO_FRONT = 3
TRIGGER_FRONT = 2

ECHO_BACK = 18
TRIGGER_BACK = 19

ECHO_LEFT = 12
TRIGGER_LEFT = 11

ECHO_RIGHT = 15
TRIGGER_RIGHT = 14

triggerfront = Pin(TRIGGER_FRONT, Pin.OUT)
echofront = Pin(ECHO_FRONT, Pin.IN)

triggerback = Pin(TRIGGER_BACK, Pin.OUT)
echoback = Pin(ECHO_PIN2, Pin.IN)

triggerleft = Pin(TRIGGER_LEFT, Pin.OUT)
echoleft = Pin(ECHO_BACK, Pin.IN)

triggerright = Pin(TRIGGER_RIGHT, Pin.OUT)
echoright = Pin(ECHO_RIGHT, Pin.IN)

tx_pin = machine.Pin(4)  # Pin number for TX on Raspberry Pi Pico
rx_pin = machine.Pin(5)  # Pin number for RX on Raspberry Pi Pico

uart = machine.UART(1, baudrate=9600, tx=tx_pin, rx=rx_pin)  # Initialize UART with custom TX and RX pins and baudrate 9600
uart.init(9600, bits=8, parity=None, stop=1)

MPU_PICO = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
imu = MPU6050(MPU_PICO)

# Define the ADC pin connected to the AOUT pin of the MQ135 sensor
adc = ADC(0)

# Calibration values for the MQ135 sensor
CALIBRATION_RL_VALUE = 10.0  # Resistance of the load resistor (RL) in Kohms
CALIBRATION_RZERO_VAL

# Function to convert ADC value to voltage
def adc_to_voltage(adc_value):
    return adc_value * 3.3 / 65535

# Function to read gas concentration from the MQ135 sensor
def read_gas_concentration():
    adc_value = adc.read_u16()
    voltage = adc_to_voltage(adc_value)
    r_sensing = CALIBRATION_RL_VALUE * voltage / (3.3 - voltage)
    ratio = r_sensing / CALIBRATION_RZERO_VALUE
    concentration = 1291 * (ratio ** -1.58)  # Using the calibration equation for CO2 gas
    return concentration

def measure_distance():
    triggerfront.low()
    sleep_us(2)
    triggerfront.high()
    sleep_us(10)
    triggerfront.low()
    pulse_durationfront = time_pulse_us(echofront, Pin.high)
    distancefront = pulse_durationfront * 0.0343 / 2
    
    triggerback.low()
    sleep_us(2)
    triggerback.high()
    sleep_us(10)
    triggerback.low()
    pulse_durationback = time_pulse_us(echoback, Pin.high)
    distanceback = pulse_durationback * 0.0343 / 2
    
    triggerleft.low()
    sleep_us(2)
    triggerleft.high()
    sleep_us(10)
    triggerleft.low()
    pulse_durationleft = time_pulse_us(echoleft, Pin.high)
    distanceleft = pulse_durationleft * 0.0343 / 2
    
    triggerright.low()
    sleep_us(2)
    triggerright.high()
    sleep_us(10)
    triggerright.low()
    pulse_durationright = time_pulse_us(echoright, Pin.high)
    distanceright = pulse_durationright * 0.0343 / 2
    out_idat = [distancefront, distanceback, distanceleft, distanceright]
    return out_idat

while True:
    # for pico reciving
    if uart.any():
        data = uart.read(1)
        if data is not None:
            received_byte = int.from_bytes(data, 'big')
            print("Received byte: {}".format(received_byte))

    # for pico sending    
    data = 30  # Data to send
    data = bytes(" ", 'utf-8')
    uart.write(data)  # Send data over UART
    utime.sleep(1)  # Delay for 1 second

    # Ultrasonic distance measurement
    print("Running")
    distance_need = measure_distance()
    print(type(distance_need))
    print("Distance1: {:.2f} cm".format(distance_need[0]))
    print("Distance2: {:.2f} cm".format(distance_need[1]))
    print("Distance3: {:.2f} cm".format(distance_need[2]))
    print("Distance4: {:.2f} cm".format(distance_need[3]))

    # MPU code
    ax=round(imu.accel.x,2)
    ay=round(imu.accel.y,2)
    az=round(imu.accel.z,2)
    gx=round(imu.gyro.x)
    gy=round(imu.gyro.y)
    gz=round(imu.gyro.z)
    tem=round(imu.temperature,2)
    print("ax",ax,"\t","ay",ay,"\t","az",az,"\t","gx",gx,"\t","gy",gy,"\t","gz",gz,"\t","Temperature",tem,"        ",end="\r")
    sleep(0.2) 

    # BMP 280 code

    print("loop is running")
    bme = BME280.BME280(i2c=i2c)
    print("bme var done")
    temp = bme.temperature
    ## hum = bme.humidity      No humidity in BMP280
    pres = bme.pressure
    # tempf temp Fahrenheit
    tempf = (bme.read_temperature()/100) * (9/5) + 32
    tempf = str(round(tempf, 2)) + 'F'
    print('Temperature:', temp ,tempf, '  Pressure: ',pres)
    #print('Humidity: ', hum)
    sleep(2)

    # MQ 135
    gas_concentration = read_gas_concentration()
    print("Gas Concentration: {:.2f} ppm".format(gas_concentration))
    utime.sleep(1)
