from machine import Pin, time_pulse_us
from time import sleep_us, sleep

ECHO_PIN1 = 9
TRIGGER_PIN1 = 8

ECHO_PIN2 = 11
TRIGGER_PIN2 = 12

ECHO_PIN3 = 7
TRIGGER_PIN3 = 6

ECHO_PIN4 = 5
TRIGGER_PIN4 = 4

trigger1 = Pin(TRIGGER_PIN1, Pin.OUT)
echo1 = Pin(ECHO_PIN1, Pin.IN)

trigger2 = Pin(TRIGGER_PIN2, Pin.OUT)
echo2 = Pin(ECHO_PIN2, Pin.IN)

trigger3 = Pin(TRIGGER_PIN3, Pin.OUT)
echo3 = Pin(ECHO_PIN3, Pin.IN)

trigger4 = Pin(TRIGGER_PIN4, Pin.OUT)
echo4 = Pin(ECHO_PIN4, Pin.IN)

def measure_distance():
    trigger1.low()
    sleep_us(2)
    trigger1.high()
    sleep_us(10)
    trigger1.low()
    pulse_duration1 = time_pulse_us(echo1, Pin.high)
    distance1 = pulse_duration1 * 0.0343 / 2
    
    trigger2.low()
    sleep_us(2)
    trigger2.high()
    sleep_us(10)
    trigger2.low()
    pulse_duration2 = time_pulse_us(echo2, Pin.high)
    distance2 = pulse_duration2 * 0.0343 / 2
    
    trigger3.low()
    sleep_us(2)
    trigger3.high()
    sleep_us(10)
    trigger3.low()
    pulse_duration3 = time_pulse_us(echo3, Pin.high)
    distance3 = pulse_duration3 * 0.0343 / 2
    
    trigger4.low()
    sleep_us(2)
    trigger4.high()
    sleep_us(10)
    trigger4.low()
    pulse_duration4 = time_pulse_us(echo4, Pin.high)
    distance4 = pulse_duration4 * 0.0343 / 2
    out_idat = [distance1, distance2, distance3, distance4]
    return out_idat

def main():
    while True:
        print("Running")
        distance_need = measure_distance()
        print(type(distance_need))
        print("Distance1: {:.2f} cm".format(distance_need[0]))
        print("Distance2: {:.2f} cm".format(distance_need[1]))
        print("Distance3: {:.2f} cm".format(distance_need[2]))
        print("Distance4: {:.2f} cm".format(distance_need[3]))
        
        sleep(0.5)

if __name__ == "__main__":
    main()
