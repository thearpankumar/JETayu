from machine import Pin, I2C
from time import sleep
from bme280 import BME280

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
bme = BME280(i2c = i2c)
print(bme.values)

