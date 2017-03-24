# -*- coding: UTF-8 -*-

import os
import sys
from libs.BaiduVoiceAPI import BaiduVoiceAPI


def main():
    # 重载系统编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 开启录音
    os.system("arecord -D 'plughw:1,0' -f S16_LE -d 3 -r 16000 tmp/voice.wav")

    # 初始化百度语音 API 工具类
    baiduVoice = BaiduVoiceAPI()

    # 开始进行语音识别
    result = baiduVoice.vocieTranslation("tmp/voice.wav")

    # 处理识别结果
    print ">>>>> 识别结果: " + result
    if (result != ""):
        # 获取语音合成 url
        voiceUrl = baiduVoice.vocieGeneration(result)
        os.system("mplayer '%s'" % voiceUrl)

if __name__ == '__main__':
    main()
