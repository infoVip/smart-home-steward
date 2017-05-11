# -*- coding: UTF-8 -*-

import os
import sys
from libs.Interact import Interact


def main():
    # 重载系统编码
    reload(sys)
    sys.setdefaultencoding("utf-8")

    # 初始化用户交互工具类
    interact = Interact()

    # 播放欢迎词
    interact.sayHello()

    # 开始服务
    interact.startServe()

if __name__ == '__main__':
    main()
