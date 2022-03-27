# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import *
import music
import WOM_Sensor_Kit

people_1 = Image("00900:09990:90909:09090:09090")
people_2 = Image("00900:09990:90909:09090:90009")

while True:
    if WOM_Sensor_Kit.WOM_pir(pin2) == 1:
        display.show(people_1)
        sleep(1000)
        display.show(people_2)
        sleep(1000)
        music.play(music.CHASE)
        display.show(people_1)
        sleep(1000)
        display.show(people_2)
        sleep(1000)
    if WOM_Sensor_Kit.WOM_pir(pin2) == 0:
        display.show(Image.YES)
