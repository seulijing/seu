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
    res = re.findall(r'\d+(?:\.\d+)?mg/100ml|\d+(?:\.\d+)?mg／100ml|\每百毫升.+\毫克|\d+(?:\.\d+)?mg／ml|\d+(?:\.\d+)?mg/100m1|'
                     r'\d+(?:\.\d+)?mg（乙醇）／ml（血液）|\d+(?:\.\d+)?mg／100mL|\d+(?:\.\d+)?毫克/100毫升|\d+(?:\.\d+)?mg/dl|'
                     r'\d+(?:\.\d+)?毫克／毫升|\d+(?:\.\d+)?mg/1OOml|\每100毫升血液中酒精含量为.+\毫克', sentence)
    for item in res:
        result.write(item + ' ')
    num = num + 1
