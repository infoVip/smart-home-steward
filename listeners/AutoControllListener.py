# -*- coding: UTF-8 -*-

import os
import sys
import time
import bluetooth
import RPi.GPIO as GPIO

sys.path.append('/home/pi/Documents/smart-home-steward/')
from libs.ADC0832API import ADC0832API

# 热释电红外引脚
pin = 24

# 光强阈值
threshold = 20

adc = ADC0832API()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def loop():
    while True:
        if GPIO.input(pin) == 1 :
            if adc.read_adc(1) < 135 :
                btInstance = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                btInstance.connect(('20:15:01:30:04:07', 1))
                btInstance.send('on')
                btInstance.close()
                time.sleep(1)
            else :
                btInstance = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                btInstance.connect(('20:15:01:30:04:07', 1))
                btInstance.send('off')
                btInstance.close()
                time.sleep(1)
        else :
            btInstance = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            btInstance.connect(('20:15:01:30:04:07', 1))
            btInstance.send('off')
            btInstance.close()
            time.sleep(1)

setup()
loop()
