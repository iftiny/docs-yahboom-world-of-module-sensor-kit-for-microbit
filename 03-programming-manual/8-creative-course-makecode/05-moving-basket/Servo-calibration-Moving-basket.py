from microbit import *
import WOM_Sensor_Kit

while True:
    WOM_Sensor_Kit.WOM_servo360(pin1, 220)
    display.show(5)
