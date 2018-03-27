# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告民族\\民族\\'
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
    res = re.findall(r'壮族|藏族|裕固族|彝族|瑶族|锡伯族|乌孜别克族|维吾尔族|佤族|土家族|土族|塔塔尔族|塔吉克族|水族|畲族|撒拉族'
                     r'羌族|普米族|怒族|纳西族|仫佬族|苗族|蒙古族|门巴族|毛南族|满族|珞巴族|僳僳族|黎族|拉祜族|柯尔克孜族|景颇族|'
                     r'京族|基诺族|回族|赫哲族|哈萨克族|哈尼族|仡佬族|高山族|鄂温克族|俄罗斯族|鄂伦春族|独龙族|东乡族|侗族|德昂族|傣族|'
                     r'达斡尔族|朝鲜族|布依族|布朗族|保安族|白族|阿昌族|汉族', sentence)
    for item in res:
        result.write(item + ' ')
    source.close()
    result.close()
    num = num + 1
