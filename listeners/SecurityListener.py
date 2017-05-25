# -*- coding: UTF-8 -*-

import os
import time
import RPi.GPIO as GPIO

# 热释电红外引脚
pin = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def loop():
    while True:
        if GPIO.input(pin) == 1 :
            # 语音警报
            os.system("mplayer 'audio/alert_security.wav'")
            os.system("mplayer 'audio/warning_security.wav'")
            # 短信通知

        else :
            time.sleep(1)

setup()
loop()
