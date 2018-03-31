# -*- coding:utf-8 -*-
import os
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\犯罪记录\\'
num = 1
total = 0
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    resName = path + str(name) + ".txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = open(resName, 'w')
    sentence = source.read()
    res = re.findall(r'\因.+?\行政拘留|\因.+?\罚款', sentence)
    for item in res:
        total = total + 1
        result.write(item + ' ')
    source.close()
    result.close()
    print(res)
    num = num + 1
print(total)
