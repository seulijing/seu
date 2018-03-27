# -*- coding:utf-8 -*-

import os
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\户籍所在地\\'
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
    res = re.findall(r'\出生于.+?\省|\,.+?\省|\出生于.+?\自治区|\出生于.+?\市|\,.+?\自治区'
                     r'\户籍所在地.+?\省|\户籍所在地.+?\自治区|\户籍所在地.+?\市'
                     r'\户籍地址：.+?\省|\户籍地址：.+?\市', sentence)
    for item in res:
        print(res)
        result.write(item + ' ')
    source.close()
    result.close()
    num = num + 1
