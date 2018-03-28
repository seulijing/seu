# -*- coding:utf-8 -*-
import os
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\居住地\\'
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
    res = re.findall(r'\现住.+?\省|\,.+\省|\现住.+？\自治区|\现住.+？\市'
                     r'\家住.+？\省|\家住.+?\自治区|\家住.+?\市'
                     r'\住：.+?\省|\住：.?\自治区|\住.+?\市', sentence)
    for item in res:
        result.write(item + ' ')
    source.close()
    result.close()
    print(res)
    num = num + 1
