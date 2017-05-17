# # -*- coding: UTF-8 -*-
#
# import RPi.GPIO as GPIO
# import time
#
# # 设置通信引脚为 GPIO 17
# pin = 12
#
# def setup():
#     # 设置树莓派引脚模式为物理定位方式
# 	GPIO.setmode(GPIO.BOARD)
#     # 设置GPIO 17引脚模式为输入模式
#     GPIO.pinMode(pin, 0)
#
# def loop():
# while True:
# 		  # 在感应范围内检测到人体
# 		  If GPIO.digitalRead(pin) == 1:
#
#             # 家庭主人已离开家庭
#             If hadLeftHome() == 1:
#                 # 触发警报，同时进入短信发送流程或声音报警流程
# 		  	      print 'Danger!'
# 	  	  else :
# 			  time.sleep(0.5)
#
# setup()
# loop()

# -*- coding: UTF-8 -*-

from libs.ADC0832API import ADC0832API

adc = ADC0832API()
tmp = adc.read_adc(1)
print tmp
