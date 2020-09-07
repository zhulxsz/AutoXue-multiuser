#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@project: AutoXue
@file: __main__.py
@author: kessil
@contact: https://github.com/kessil/AutoXue/
@time: 2019-10-26(星期六) 10:22
@Copyright © 2019. All rights reserved.
"""
import subprocess
from argparse import ArgumentParser
import time
from . import App
from .unit import logger, caps
from .secureRandom import SecureRandom as random
import sys


# parse = ArgumentParser(description="Accept username and password if necessary!")
#
# parse.add_argument("-u", "--username", metavar="username", type=str, default='', help='User Name')
# parse.add_argument("-p", "--password", metavar="password", type=str, default='', help='Pass Word')
# args = parse.parse_args()
# app = App(args.username, args.password)


def shuffle(funcs):
    random.shuffle(funcs)
    for func in funcs:
        func()
        time.sleep(5)


def start():
    # if random.random() > 0.5:
    #     logger.debug(f'视听学习优先')
    #     app.watch()
    #     app.music()
    #     shuffle([app.read, app.daily, app.challenge, app.weekly])
    # else:
    logger.debug(f'视听学习置后')
    app.music()
    shuffle([app.daily, app.challenge, app.read, app.weekly])
    app.view_score()
    app.watch()
    app.logout_or_not()
    app.driver.close_app()
    # app.driver.quit()


def test():
    app.weekly()
    logger.info(f'测试完毕')

# 循环刷题
def recycle_main_do():
    t = time.time()
    while True:
        try:
            start()
            break
        except Exception as ex:
            print("出现如下异常%s" % ex)
            app.logout_or_not()
            app.driver.close_app()
            if time.time() - t > 3600:
                print('程序存在错误，试了一个小时都不行，换下个号码刷')
                break


if __name__ == "__main__":
    user_list = [
        ['17660082669', 'Nopass.123'],
        ['18605315732', '000000'],
        ['17753166732', '000000'],
    ]
    for index_u, user in enumerate(user_list):
        # 定义一个APP的启动时间，超时1小时换下一个
        t = time.time()
        while True:
            try:
                app = App(user[0], user[1])
                start()
                break
            except Exception as ex:
                logger.info(f'刷分出现如下异常%s' % ex)
                try:
                    app.logout_or_not()
                    app.driver.close_app()
                except Exception as ex:
                    logger.info(f'退出APP出现如下异常%s' % ex)
                continue
                if time.time() - t > 3600:
                    print('程序存在错误，试了一个小时都不行，换下个号码刷')
                    logger.info(f'程序存在错误，试了一个小时都不行，换下个号码刷')
                    break
    # start()
    sys.exit(0)
    # test()
