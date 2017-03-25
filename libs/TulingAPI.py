# -*- coding: UTF-8 -*-

import os
import json
import urllib2
import traceback
import ConfigParser


class TulingAPI():
    # 图灵 API 基本参数
    apiKey = ""

    # 初始化模块
    def __init__(self):
        # 读取配置
        print "***** 读取图灵配置信息 *****"

        self.config = ConfigParser.ConfigParser()
        self.config.read("./app.conf")
        self.apiKey = self.config.get("TulingAPI", "apiKey")

        if (self.apiKey == ""):
            print '\033[1;31;40m'
            print "!!!!! 图灵配置信息加载失败，请检查配置文件是否正确！ !!!!!"
            print '\033[0m'
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

    # 图灵对话接口请求
    def getDialogResult(self, text):
        print "***** 请求图灵对话接口 *****"

        # 构造 get url
        url = "http://www.tuling123.com/openapi/api?key=" + self.apiKey + "&info=" + text

        # 请求对话结果
        result = self.request(url, "")

        # 仅处理结果为文本类型的响应
        if (result["code"] == 100000):
            return result["text"]
        else:
            print "***** 对话结果为非文字类型，不予处理！ *****"
            return ""
