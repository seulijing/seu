# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\分类\\醉驾\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\酒精浓度\\'
num = 1
while num <= 80:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    resName = path + str(name) + ".txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = open(resName, 'w')
    sentence = source.read()
    res = re.findall(r'\d+(?:\.\d+)?mg/|\d+(?:\.\d+)?mg／|\每百毫升.+\毫克|\d+(?:\.\d+)?mg／ml|\d+(?:\.\d+)?mg/|'
                     r'\d+(?:\.\d+)?mg（乙醇）／ml（血液）|\d+(?:\.\d+)?mg／|\d+(?:\.\d+)?毫克/|\d+(?:\.\d+)?mg/dl|'
                     r'\d+(?:\.\d+)?毫克／毫升|\d+(?:\.\d+)?mg/|\为.+\毫克', sentence)
    for item in res:
        res1 = re.findall(r'\d{2,3}.\d{1,2}|\d{2,3}', item)
        print(num, res1)
    source.close()
    result.close()
    num = num + 1
