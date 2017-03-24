# -*- coding: UTF-8 -*-

import os
import json
import time
import base64
import urllib2
import traceback
import ConfigParser


class BaiduVoiceAPI():
    # 百度语音 API 基本参数
    config = ""
    cuid = ""
    apiKey = ""
    secretKey = ""
    accessToken = ""

    # 百度语音识别参数
    rate = ""
    audioFormat = ""
    recognizeLanguage = ""

    # 百度语音合成参数
    pitch = ""
    speed = ""
    volumn = ""
    person = ""
    generationLanguage = ""

    # 初始化模块
    def __init__(self):
        # 读取配置
        print "***** 读取配置信息 *****"

        self.config = ConfigParser.ConfigParser()
        self.config.read("./app.conf")
        self.cuid = self.config.get("BaiduVoiceAPI", "cuid")
        self.apiKey = self.config.get("BaiduVoiceAPI", "apiKey")
        self.secretKey = self.config.get("BaiduVoiceAPI", "secretKey")
        self.accessToken = self.config.get("BaiduVoiceAPI", "accessToken")
        self.expireAt = self.config.get("BaiduVoiceAPI", "expireAt")

        self.rate = self.config.get("BaiduVoiceRecognition", "rate")
        self.audioFormat = self.config.get("BaiduVoiceRecognition", "format")
        self.recognizeLanguage = self.config.get(
            "BaiduVoiceRecognition", "recognizeLanguage")

        self.pitch = self.config.get("BaiduVoiceGeneration", "pitch")
        self.speed = self.config.get("BaiduVoiceGeneration", "speed")
        self.volumn = self.config.get("BaiduVoiceGeneration", "volumn")
        self.person = self.config.get("BaiduVoiceGeneration", "person")
        self.generationLanguage = self.config.get(
            "BaiduVoiceGeneration", "generationLanguage")

        if (self.cuid == "") or (self.apiKey == "") or (self.secretKey == "") or (self.rate == "") or (self.audioFormat == "") or (self.recognizeLanguage == ""):
            print "!!!!! 配置信息加载失败，请检查配置文件是否正确！ !!!!!"
            os._exit(0)

        # 加载 accessToken
        try:
            # 如果 accessToken 不存在或者过期则重新获取
            if (self.expireAt == "") or (self.accessToken == "") or (int(time.time()) > int(self.expireAt)):
                print "***** 请求 Access Token *****"
                self.getToken()
        except Exception, e:
            traceback.print_exc()
            os._exit(0)

    # 发起请求
    def request(self, url, data):
        try:
            response = urllib2.urlopen(url=url, data=json.dumps(data))
            jsonData = json.loads(response.read())
            return jsonData
        except Exception, e:
            traceback.print_exc()
            os._exit(0)

    # 获取 accessToken
    def getToken(self):
        authUrl = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (
            self.apiKey, self.secretKey)
        response = self.request(authUrl, '')
        self.accessToken = response['access_token']
        self.expireAt = str(int(time.time()) + int(response['expires_in']))

        # 保存accessToken
        self.config.set("BaiduVoiceAPI", "accessToken", self.accessToken)
        self.config.set("BaiduVoiceAPI", "expireAt", self.expireAt)
        # 写回配置文件
        self.config.write(open("./app.conf", "w"))

    # 语音识别接口请求
    def vocieTranslation(self, audioFile):
        print "***** 请求语音识别接口 *****"
        apiUrl = "http://vop.baidu.com/server_api"

        fileLen = os.path.getsize(audioFile)
        audioFile = open(audioFile, 'rb')
        encryptData = base64.b64encode(audioFile.read())
        audioFile.close()

        # 封装 post 请求并发送
        postBody = {'format': self.audioFormat, 'rate': self.rate, 'channel': 1, 'lan': self.recognizeLanguage,
                    'token': self.accessToken, 'cuid': self.cuid, 'len': fileLen, 'speech': encryptData}
        response = self.request(apiUrl, postBody)

        # 结果处理
        if (response['err_no'] == 0):
            return response['result'][0]
        else:
            print response['err_msg']
            return ""

    # 语音合成接口请求
    def vocieGeneration(self, text):
        print "***** 请求语音合成接口 *****"

        # 构造 get url
        url = "http://tsn.baidu.com/text2audio?tex=" + text + \
            "&lan=" + self.generationLanguage + "&tok=" + self.accessToken + \
            "&ctp=1&cuid=" + self.cuid + "&spd=" + self.speed + "&pit=" + \
            self.pitch + "&vol=" + self.volumn + "&person=" + self.person

        return url
