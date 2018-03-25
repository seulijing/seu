# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\醉驾\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\醉驾1\\'
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
    res = re.findall(r'\d+(?:\.\d+)?mg/100ml', sentence)
    res1 = re.findall(r'\d+(?:\.\d+)?mg／100ml', sentence)
    res2 = re.findall(r'\每百毫升.+\毫克', sentence)
    res3 = re.findall(r'\d+(?:\.\d+)?mg／ml', sentence)
    res4 = re.findall(r'\d+(?:\.\d+)?mg/100m1', sentence)
    res5 = re.findall(r'\d+(?:\.\d+)?mg（乙醇）／ml（血液）', sentence)
    res6 = re.findall(r'\d+(?:\.\d+)?mg／100mL', sentence)
    res7 = re.findall(r'\d+(?:\.\d+)?毫克/100毫升', sentence)
    res8 = re.findall(r'\d+(?:\.\d+)?mg/dl', sentence)
    res9 = re.findall(r'\d+(?:\.\d+)?毫克／毫升', sentence)
    res10 = re.findall(r'\d+(?:\.\d+)?lmg/1OOml', sentence)
    res11 = re.findall(r'\每100毫升血液中酒精含量为.+\毫克', sentence)
    result.writelines(res)
    result.writelines(res1)
    result.writelines(res2)
    result.writelines(res3)
    result.writelines(res4)
    result.writelines(res5)
    result.writelines(res6)
    result.writelines(res7)
    result.writelines(res8)
    result.writelines(res9)
    result.writelines(res10)
    result.writelines(res11)
    num = num + 1
# print(re.findall(r'\d+(?:\.\d+)?mg/100ml', sentence))
# print(re.findall(r'\人民币.+\元', sentence))

