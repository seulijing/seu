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
        res = re.findall(r'河北省|山西省|辽宁省|吉林省|黑龙江省|江苏省|浙江省|安徽省|福建省|江西省|山东省|河南省|'
                         r'湖北省|湖南省|广东省|海南省|四川省|贵州省|云南省|陕西省|甘肃省|青海省|台湾省|北京市|上海市|重庆市|天津市|'
                         r'广西壮族自治区|宁夏回族自治区|西藏自治区|新疆维吾尔自治区|内蒙古自治区', sentence)
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
