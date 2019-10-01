'''
游戏: Hi Lo
'''
import time
import os
import random

def game():
    print('================ Hi Lo ================')
    rightNumber = random.randint(0, 1000)
    inputNumber = 0
    l1 = 0
    l2 = 1000
    while True:
        inputNumber = int(input('输入一个{}~{}的数：'.format(l1, l2)))
        while inputNumber != rightNumber:
            if inputNumber > rightNumber:
                l2 = inputNumber
                inputNumber = int(input('输入一个{}~{}的数：'.format(l1, l2)))

            else:
                l1 = inputNumber
                inputNumber = int(input('输入一个{}~{}的数：'.format(l1, l2)))

        break
    print('答对了')