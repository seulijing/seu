# -*- coding:utf-8 -*-
import codecs
import os
import re
import shutil
import jieba
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告性别\\男\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告性别\\女\\'
num = 1
total1 = 0
total2 = 0
output = ''


def sex():
    global num, output
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        a()
        res = re.findall(r'男|女', output)
        for item in res:
            if item == '男':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if item == '女':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
        output = ''
        num = num + 1


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
    labels = ['男', '女']
    plt.bar(range(len(data)), data, tick_label=labels)
    plt.title('被告人性别信息柱状图')
    plt.ylim(0, 80)
    plt.show()


if __name__ == '__main__':
    sex()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    print("男：", total1)
    print("女：", total2)
    b()
