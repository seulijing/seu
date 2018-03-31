# -*- coding:utf-8 -*-
import os
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
num = 1
total = 0
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    sentence = source.read()
    res = re.findall(r'从重', sentence)
    for item in res:
        total = total + 1
        break
    source.close()
    print(res)
    num = num + 1
print(total)
