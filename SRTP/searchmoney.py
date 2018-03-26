# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\罚金\\'
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    resName = path + str(name) + ".txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = open(resName, 'w')
    sentence = source.read()
    res = re.findall(r'\人民币.+\元|\罚金.+\元', sentence)
    for item in res:
        result.write(item + ' ')
    source.close()
    result.close()
    num = num + 1
