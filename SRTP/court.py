# -*- coding:utf-8 -*-
import os
import re
import shutil

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\初级\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\中级\\'
path3 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\高级\\'
path4 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\最高\\'
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    sentence1 = source.readlines()[0]
    source.close()
    source = open(fileName, 'r')
    sentence2 = source.readlines()[1]
    sentence = sentence1 + sentence2
    res = re.findall(r'区人民法院|县人民法院|市人民法院|省人民法院|中级人民法院|初级人民法院|高级人民法院|最高人民法院', sentence)
    for item in res:
        if (item == '区人民法院') | (item == '县人民法院') | (item == '初级人民法院'):
            resname1 = path1 + str(name) + ".txt"
            if os.path.exists(resname1):
                os.remove(resname1)
            shutil.copyfile(fileName, resname1)
        if (item == '市人民法院') | (item == '中级人民法院'):
            resname2 = path2 + str(name) + ".txt"
            if os.path.exists(resname2):
                os.remove(resname2)
            shutil.copyfile(fileName, resname2)
        if (item == '省人民法院') | (item == '高级人民法院'):
            resname3 = path3 + str(name) + ".txt"
            if os.path.exists(resname3):
                os.remove(resname3)
            shutil.copyfile(fileName, resname3)
        if (item == '最高人民法院'):
            resname4 = path4 + str(name) + ".txt"
            if os.path.exists(resname4):
                os.remove(resname4)
            shutil.copyfile(fileName, resname4)
    num = num + 1
