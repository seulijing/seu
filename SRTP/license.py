# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\无牌照\\'
num = 1
total = 1
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
        res = re.findall(r'无牌照', sentence)
        for item in res:
            result.write(item + ' ')
            total = total + 1
            break
        source.close()
        result.close()
    num = num + 1
print(total)
