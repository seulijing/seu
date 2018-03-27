# -*- coding:utf-8 -*-
import codecs
import os
import re
import shutil
import jieba
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告民族\\汉族\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告民族\\少数民族\\'
num = 1
total1 = 0
total2 = 0
output = ''


def nation():
    global num, output
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    a()
    res = re.findall(r'壮族|藏族|裕固族|彝族|瑶族|锡伯族|乌孜别克族|维吾尔族|佤族|土家族|土族|塔塔尔族|塔吉克族|水族|畲族|撒拉族'
                     r'羌族|普米族|怒族|纳西族|仫佬族|苗族|蒙古族|门巴族|毛南族|满族|珞巴族|僳僳族|黎族|拉祜族|柯尔克孜族|景颇族|'
                     r'京族|基诺族|回族|赫哲族|哈萨克族|哈尼族|仡佬族|高山族|鄂温克族|俄罗斯族|鄂伦春族|独龙族|东乡族|侗族|德昂族|傣族|'
                     r'达斡尔族|朝鲜族|布依族|布朗族|保安族|白族|阿昌族|汉族', output)
    for item in res:
        if item == '汉族':
            resname1 = path1 + str(name) + ".txt"
            if os.path.exists(resname1):
                os.remove(resname1)
            shutil.copyfile(fileName, resname1)
            return
    resname2 = path2 + str(name) + ".txt"
    if os.path.exists(resname2):
        os.remove(resname2)
    shutil.copyfile(fileName, resname2)
    source.close()


def a():
    global num
    global output
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    spy = {}.fromkeys([line.strip() for line in codecs.open('spy.txt')])
    for line in source:
        seglist = jieba.cut(line)
        for segs in seglist:
            if segs not in spy:
                seg = segs.lower()
                output += seg
                output += ' '
            else:
                return


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['汉族', '少数民族']
    plt.bar(range(len(data)), data, tick_label=labels)
    plt.title('被告人民族信息柱状图')
    plt.ylim(0, 100)
    plt.show()


if __name__ == '__main__':
    while num <= 100:
        name = "%d" % num
        nation()
        num = num + 1
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    print("汉族：", total1)
    print("少数民族：", total2)
    b()
