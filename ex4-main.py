# task(4)
from microbit import *
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()
while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    sleep(1000)
    pin0.write_digital(2)
    
