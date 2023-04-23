from machine import Pin, I2C
from time import sleep
from bme280 import BME280
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.move_to(0,0)
lcd.putstr("Weather Station")
lcd.move_to(0,1)
lcd.putstr("RaspberryPiPico")
bme = BME280(i2c=i2c)
print(bme.values)
t, p, h = bme.read_compensated_data()
p = p // 256
pi = p // 100
pd = p - pi * 100
hi = h // 1024
hd = h * 100 // 1024 - hi * 100
sleep(2)
lcd.clear()
while True:
    lcd.move_to(0,0)
    lcd.putstr("Weather Station")
    
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Temp: ")
    lcd.putstr(str(t/100))
    lcd.putstr(" *C")
    sleep(1.5)
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Humid: ")
    lcd.putstr("{}.{:02d} %".format(hi, hd))
    sleep(1.5)
    lcd.move_to(0,1)
    lcd.putstr("                ")
    lcd.move_to(0,1)
    lcd.putstr("Pres:")
    lcd.putstr("{}.{:02d} hPa".format(pi, pd))
    sleep(1.5)

