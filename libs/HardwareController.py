# -*- coding: UTF-8 -*-

import time
import RPi.GPIO as GPIO


class HardwareController():

    # TODO: 初始化时用列表 + 字典配置引脚输出模式

    def __init__(self):
        # BOARD编号方式，基于插座引脚编号
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        # 输出模式
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

    def lightUp(self, pin):
        GPIO.output(pin, GPIO.HIGH)

    def lightOff(self, pin):
        GPIO.output(pin, GPIO.LOW)
