# -*- coding: UTF-8 -*-

import os
import random
import ConfigParser
import Adafruit_DHT
from libs.TulingAPI import TulingAPI
from libs.BaiduVoiceAPI import BaiduVoiceAPI
from libs.HardwareController import HardwareController
from libs.MusicPlayer import MusicPlayer


class Interact():
    hardwareHelper = ""
    baiduVoice = ""
    tuling = ""

    # 唤醒欢迎词
    salutatories = ""

    # 初始化模块
    def __init__(self):
        # 初始化硬件控制类
        self.hardwareHelper = HardwareController()

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

    # 开始语音服务
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

            # 语音控制开关灯
            if ("灯" in voiceResult):
                if ("红" in voiceResult):
                    voiceUrl = self.baiduVoice.vocieGeneration("好的，正在为您开红色的灯")
                    os.system("mplayer '%s'" % voiceUrl)
                    os.system("mplayer 'audio/device_on.wav'")
                    self.hardwareHelper.lightUp(11)
                if ("黄" in voiceResult):
                    voiceUrl = self.baiduVoice.vocieGeneration("好的，正在为您开黄色的灯")
                    os.system("mplayer '%s'" % voiceUrl)
                    os.system("mplayer 'audio/device_on.wav'")
                    self.hardwareHelper.lightUp(13)
                if ("蓝" in voiceResult):
                    voiceUrl = self.baiduVoice.vocieGeneration("好的，正在为您开蓝色的灯")
                    os.system("mplayer '%s'" % voiceUrl)
                    os.system("mplayer 'audio/device_on.wav'")
                    self.hardwareHelper.lightUp(15)
                if ("关" in voiceResult):
                    voiceUrl = self.baiduVoice.vocieGeneration("好的，正在为您关灯")
                    os.system("mplayer '%s'" % voiceUrl)
                    os.system("mplayer 'audio/device_off.wav'")
                    self.hardwareHelper.lightOff(11)
                return

            # 测量室内温湿度数据
            if ("室内" in voiceResult or "温度" in voiceResult or "湿度" in voiceResult):
                voiceUrl = self.baiduVoice.vocieGeneration("正在监测室内温湿度，请稍候")
                os.system("mplayer '%s'" % voiceUrl)
                os.system("mplayer 'audio/loading.wav'")

                # 获取室内温湿度
                humidity, temperature = Adafruit_DHT.read_retry(22, 4)

                voiceUrl = self.baiduVoice.vocieGeneration("当前室内温度为，'%.1f'度，湿度为，'%.1f'%%RH" % (temperature, humidity))
                os.system("mplayer '%s'" % voiceUrl)
                return

            # 播放歌曲
            if ("播放" in voiceResult):
                musicName = voiceResult[voiceResult.find('播放'):voiceResult.find('，')]

                voiceUrl = self.baiduVoice.vocieGeneration("好哒，正在为您播放'%s'" % musicName[2: ])
                os.system("mplayer '%s'" % voiceUrl)

                # 播放指定歌曲
                music = MusicPlayer()
                music.play(musicName[2: ])



                return

            # 请求图灵对话结果
            dialogResult = self.tuling.getDialogResult(voiceResult)
            print '\033[1;32;40m'
            print ">>>>> 图灵对话结果: " + dialogResult
            print '\033[0m'
            # 获取语音合成 url
            voiceUrl = self.baiduVoice.vocieGeneration(dialogResult)
            os.system("mplayer '%s'" % voiceUrl)

    def hardwareControl(self):
        return
