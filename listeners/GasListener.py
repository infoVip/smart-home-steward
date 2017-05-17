# -*- coding: UTF-8 -*-

import os
import sys
import time

sys.path.append('/home/pi/Documents/smart-home-steward/')
from libs.ADC0832API import ADC0832API
from libs.BaiduVoiceAPI import BaiduVoiceAPI

# 燃气浓度阈值
threshold = 20
adc = ADC0832API()

def loop():
    while True:
        tmp = adc.read_adc(0)
        if tmp > threshold :
            os.system("mplayer 'audio/alert.wav'")
            os.system("mplayer 'audio/warning_gas.wav'")
        else :
            time.sleep(1)
loop()
