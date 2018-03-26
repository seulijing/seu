# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\分类\\追逐竞驶\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\速度\\'
num = 1
while num <= 12:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    resName = path + str(name) + ".txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = open(resName, 'w')
    sentence = source.read()
    res = re.findall(r'\d+(?:\.\d+)?km/h|\d+(?:\.\d+)?公里／小时|\d+(?:\.\d+)?km／h', sentence)
    for item in res:
        result.write(item + ' ')
    source.close()
    result.close()
    num = num + 1
