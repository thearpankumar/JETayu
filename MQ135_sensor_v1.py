"""
MQ-135 DETECTS MULTIPLE GASES!!!!!!!!!!!!!1
DETECTS -----> NH3, NOx, Alcohol, Benzene, Smoke, CO2
CANNOT DETECT ONE SPECIFIC GAS
"""

from machine import Pin, time_pulse_us
from time import sleep_us, sleep

A_SENSOR_VALUE = machine.ADC(31)                   # any adcc pin

sleep(20)

while True:
    reading = A_SENSOR_VALUE.read_u16()
    print("ADC: ", reading)
    sleep(0.4)
    if reading > 800:                              #change value based on analogue value obtained in the presence of ammonia
        print("\t\t AMMONIA DETECTED")
       
