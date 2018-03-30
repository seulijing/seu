# -*- coding:utf-8 -*-
import re
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\因酒驾受过行政处罚\\'
num = 1
total1 = 0



def response():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'\因酒后驾驶.+?\行政拘留|\因酒后驾驶.+?\行政罚款', sentence)
        for item in res:
            resname1 = path1 + str(name) + ".txt"
            if os.path.exists(resname1):
                os.remove(resname1)
            shutil.copyfile(fileName, resname1)
        num = num + 1


if __name__ == '__main__':
    response()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    print("因酒驾受过行政处罚：", total1)