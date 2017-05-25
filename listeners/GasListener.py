# -*- coding: UTF-8 -*-

import os
import sys
import time
import urllib2

sys.path.append('/home/pi/Documents/smart-home-steward/')
from libs.ADC0832API import ADC0832API

# 燃气浓度阈值
threshold = 40 
adc = ADC0832API()

def loop():
    while True:
        if adc.read_adc(0) > threshold :
            # 语音警报
            os.system("mplayer 'audio/alert_gas.wav'")
            os.system("mplayer 'audio/warning_gas.wav'")
            # 短信通知
            urllib2.urlopen('http://sh.zark.in/alert/gas')
        else :
            time.sleep(1)
loop()
