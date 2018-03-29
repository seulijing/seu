# -*- coding:utf-8 -*-
import re
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\态度\\自首\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\态度\\立功\\'
num = 1
total1 = 0
total2 = 0


def ifdie():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        sentence = sentence.replace('处理自首和立功', '')
        if ("没有自首、立功的情节" not in sentence) & ("不能认定为具有立功情节" not in sentence):
            res = re.findall(r'自首|立功', sentence)
            for item in res:
                if item == '自首':
                    resname1 = path1 + str(name) + ".txt"
                    if os.path.exists(resname1):
                        os.remove(resname1)
                    shutil.copyfile(fileName, resname1)
                if item == '立功':
                    resname2 = path2 + str(name) + ".txt"
                    if os.path.exists(resname2):
                        os.remove(resname2)
                    shutil.copyfile(fileName, resname2)
        source.close()
        num = num + 1


def remove():
    num1 = 1
    num2 = 1
    while num1 <= 100:
        name = "%d" % num1
        fileName1 = path1 + str(name) + ".txt"
        if os.path.exists(fileName1):
            source1 = open(fileName1, 'r')
            sentence1 = source1.read()
            if ("不予采纳" in sentence1) | ("驳回" in sentence1):
                source1.close()
                os.remove(fileName1)
        num1 = num1 + 1
    while num2 <= 100:
        name = "%d" % num2
        fileName2 = path2 + str(name) + ".txt"
        if os.path.exists(fileName2):
            source2 = open(fileName2, 'r')
            sentence2 = source2.read()
            if ("不予采纳" in sentence2) | ("驳回" in sentence2):
                source2.close()
                os.remove(fileName2)
        num2 = num2 + 1


if __name__ == '__main__':
    ifdie()
    remove()
    total3 = 0
    total4 = 0
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total3 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total4 += 1  # 统计文件夹下文件个数
    print("自首：", total3)
    print("立功：", total4)
