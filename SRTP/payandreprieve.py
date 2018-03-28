# -*- coding:utf-8 -*-
import re
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\赔偿缓刑\\积极赔偿\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\赔偿缓刑\\缓刑\\'
num = 1
total1 = 0


def road():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'积极赔偿|缓刑|主动赔偿', sentence)
        for item in res:
            if (item == '积极赔偿') | (item == '主动赔偿'):
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if item == '缓刑':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
        num = num + 1


def remove():
    num1 = 1
    global total1
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    while num1 <= total1:
        name = "%d" % num1
        fileName1 = path2 + str(name) + ".txt"
        if os.path.exists(fileName1):
            source1 = open(fileName1, 'r')
            sentence1 = source1.read()
            if ("不予采纳" in sentence1) | ("驳回" in sentence1):
                source1.close()
                os.remove(fileName1)
        num1 = num1 + 1


if __name__ == '__main__':
    road()
    total2 = 0
    total3 = 0
    remove()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total3 += 1  # 统计文件夹下文件个数
    print("积极赔偿：", total2)
    print("缓刑：", total3)
