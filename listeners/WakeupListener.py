# -*- coding: UTF-8 -*-

import os
import time
import serial

# 初始化串口通信
instance = serial.Serial('/dev/ttyS0', 9600, timeout=0.5)

def recv(serial):
    while True:
        data = serial.read(1)
        serial.flushInput()
        # 当接收到字符时立即返回
        if data != '':
            break
        time.sleep(1)
    return data

while True:
    data = recv(instance)
    if('@' in data):
        # 杀死所有 mplayer 音频播放
        os.system("killall mplayer")
        # 唤醒软件识别流程
        os.system("python ./handlers/VoiceHandler.py")
