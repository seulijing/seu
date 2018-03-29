# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\时间\\'
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    if os.path.exists(fileName):
        source = open(fileName, 'r')
        resName = path + str(name) + ".txt"
        if os.path.exists(resName):
            os.remove(resName)
        result = open(resName, 'w')
        sentence = source.read()
        res = re.findall(r'\d+(?:\.\d+)?时', sentence)
        list1 = sorted(set(res), key=res.index)
        for item in list1:
            result.write(item + ' ')
        source.close()
        result.close()
        print(num, list1)
    num = num + 1
