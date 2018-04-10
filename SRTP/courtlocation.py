# -*- coding:utf-8 -*-
import os
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院所在地\\'
num = 1


def courtlocation():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence1 = source.readlines()[0]
        source.close()
        source = open(fileName, 'r')
        sentence2 = source.readlines()[1]
        sentence = sentence1 + sentence2
        res = re.findall(r'河北|山西|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|'
                         r'湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾|北京|上海|重庆|天津|'
                         r'广西|宁夏|西藏|新疆|内蒙', sentence)
        resname = path + str(name) + ".txt"
        if os.path.exists(resname):
            os.remove(resname)
        result = open(resname, 'w')
        for item in res:
            result.write(item)
        source.close()
        num = num + 1


if __name__ == '__main__':
    courtlocation()
