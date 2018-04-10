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
    list1 = sorted(set(res), key=res.index)
    for a in list1:
        res1 = re.findall(r'河北|山西|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|'
                          r'湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾|北京|上海|重庆|天津|'
                          r'广西|宁夏|西藏|新疆|内蒙', a)
        for item in res1:
            print(res1)
            result.write(item + ' ')
    source.close()
    result.close()
    num = num + 1
