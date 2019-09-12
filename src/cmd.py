#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: cmd
# Auther: ZZY2357
# Time: 2019/09/08 20:28:37

import time
import os
import random

def readAsciiText(url):
    try:
        f = open(url, 'r')
        text = f.read()
        f.close()
        return text
    except BaseException as err:
        return str(err)

print(readAsciiText('asciiText/welcome.txt') + '''

欢迎来到cmd！这是一个模拟控制台的程序，模仿 http://cmd.to ，输入 $ help 查看帮助

作者：ZZY2357
QQ：3440652547
''')

def help():
    print(readAsciiText('asciiText/help.txt') + '''
* $ help \t 帮助
* $ clear \t 清空
* $ bye \t 退出
===================================
* $ cmd \t 指令
    * exc \t 做运算 使用: $ cmd exc
    * eval \t 执行 Python 语句 使用: $ cmd eval
    * reverce \t 反转句子 使用: $ cmd reverce
===================================
* $ system \t 系统
    * shutdown \t 关机 使用: $ system shutdown
    * rebot \t 重启 使用: $ system rebot
===================================
* $ game \t 游戏
    * HiLo \t 猜数游戏
''')

class Cmd:
    def exc(self):
        suanshi = _input('输入算式: ')
        price = eval(suanshi)
        print(' ==> ', price)
    def eval(self):
        cooooooooo = _input('输入语句: ')
        print(eval(cooooooooo))
    def reverce(self):
        stri = _input('输入句子: ')
        array = list(stri)
        output = ''
        for i in range(len(array), 0, -1):
            output += array[i - 1]
        print(' ==> ', output)
        
class System:
    def shutdown(self):
        os.system('shutdown -s -c "你的电脑即将关机" -t 10')
    def rebot(self):
        os.system('shutdown -r -c "你的电脑即将重启" -t 10')

class Game:
    def HiLo(self):
        rightNumber = random.randint(1, 1000)
        while True:
            userNumber = int(_input('输入一个1~1000的数: '))
            if userNumber == rightNumber:
                break
            elif userNumber > rightNumber:
                print(' ==> 大了')
            else:
                print(' ==> 小了')
        print(' ==> 答对了')
def clear():
    os.system('cls')

def bye():
    print(readAsciiText('asciiText/bye.txt'))
    exit()
    return 'Bye bye ~'

def _input(string):
    _input = input('$ ' + string)
    time.sleep(0.2)
    return _input


# main
cmd = Cmd()
game = Game()
system = System()

def countCommand(command):
    fenjie = command.split(' ')
    theCommand = ""
    for i in range(len(fenjie)):
        theCommand += fenjie[i]
        if i == len(fenjie) - 1:
            continue
        theCommand += '.'
    theCommand += '()'
    exec(theCommand)

while True:
    inputCommand = _input('')
    try:
        countCommand(inputCommand)
    except:
        print(' 错误，请检查语句是否正确或存在 ')
