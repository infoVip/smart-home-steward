# -*- coding: UTF-8 -*-

import os
import json
import base64
import urllib2
import traceback

class MusicPlayer():

    # 发起请求
    def request(self, url, data):
        try:
            response = urllib2.urlopen(url=url, data=json.dumps(data))
            jsonData = json.loads(response.read())
            return jsonData
        except Exception, e:
            traceback.print_exc()
            os._exit(0)

    # 搜索歌曲
    def play(self, name):
        listUrl = "http://mobilecdn.kugou.com/api/v3/search/song?keyword='%s'&pagesize=1" % name
        resultList = self.request(listUrl, '')
        musicUrl = "http://m.kugou.com/app/i/getSongInfo.php?hash=%s&cmd=playInfo" % resultList['data']['info'][0]['hash']
        response = self.request(musicUrl, '')
        print response['url']
        os.system("mplayer '%s' < /dev/null > /dev/null 2>1&" % response['url'])
