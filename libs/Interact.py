# -*- coding: UTF-8 -*-

import os
import random
import ConfigParser
from libs.TulingAPI import TulingAPI
from libs.BaiduVoiceAPI import BaiduVoiceAPI


class Interact():
    baiduVoice = ""
    tuling = ""

    # 唤醒欢迎词
    salutatories = ""

    # 初始化模块
    def __init__(self):
        # 初始化百度语音 API 工具类
        self.baiduVoice = BaiduVoiceAPI()

        # 初始化图灵 API 工具类
        self.tuling = TulingAPI()

        # 读取配置
        print "***** 读取交互工具类配置信息 *****"
        self.config = ConfigParser.ConfigParser()
        self.config.read("./app.conf")
        self.salutatories = self.config.items("Salutatory")

        if (len(self.salutatories) == 0):
            print '\033[1;31;40m'
            print "!!!!! 交互工具类配置信息加载失败，请检查配置文件是否正确！ !!!!!"
            print '\033[0m'
            os._exit(0)

    # 播放唤醒欢迎词
    def sayHello(self):
        # 播放音效
        os.system("mplayer 'audio/wakeup.wav'")

        # 随机抽取一句欢迎词
        salLen = len(self.salutatories)
        selectedIndex = random.randint(0, salLen - 1)
        selectedItem = self.salutatories[selectedIndex]

        # 获取语音合成 url
        voiceUrl = self.baiduVoice.vocieGeneration(selectedItem[1])
        os.system("mplayer '%s'" % voiceUrl)

    def startServe(self):
        # 开启录音
        os.system("arecord -D 'plughw:1,0' -f S16_LE -d 3 -r 16000 audio/voice.wav")

        # 开始进行语音识别
        voiceResult = self.baiduVoice.vocieTranslation("audio/voice.wav")

        # 处理识别结果
        print '\033[1;32;40m'
        print ">>>>> 识别结果: " + voiceResult
        print '\033[0m'
        if (voiceResult != ""):
            # 请求图灵对话结果
            dialogResult = self.tuling.getDialogResult(voiceResult)
            print '\033[1;32;40m'
            print ">>>>> 图灵对话结果: " + dialogResult
            print '\033[0m'
            # 获取语音合成 url
            voiceUrl = self.baiduVoice.vocieGeneration(dialogResult)
            os.system("mplayer '%s'" % voiceUrl)
