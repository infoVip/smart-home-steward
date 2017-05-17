# -*- coding: UTF-8 -*-

import os
import sys


def main():
    # 重载系统编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 启动语音唤醒监听
    os.popen("python WakeupListener.py")

    # 启动语音唤醒监听
    os.popen("python GasListener.py")

if __name__ == '__main__':
    main()
