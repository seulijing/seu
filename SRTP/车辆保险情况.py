# -*- coding:utf-8 -*-
import re
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\有保险\\'
num = 1
total1 = 0


def response():
    global num, total1
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'强制险|交强险', sentence)
        for item in res:
            if (item == "强制险") | (item == "交强险"):
                total1 += 1
                break
        num = num + 1


if __name__ == '__main__':
    response()
    print("交强险 or 强制险", total1)

