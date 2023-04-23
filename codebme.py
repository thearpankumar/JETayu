"""from machine import Pin, I2C
from time import sleep
import BME280
# PICO - Pins
# sda=Pin(16), scl=Pin(17) 
sda=machine.Pin(16)
scl=machine.Pin(17)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)
while True:
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
    sleep(2)"""


