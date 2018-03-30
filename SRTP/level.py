# -*- coding:utf-8 -*-
import codecs
import os
import re
import shutil
import jieba
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\审级\\一审\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\审级\\二审\\'
num = 1
total1 = 0
total2 = 0
output = ''


def level():
    global num, output
    fileName = filepath + str(name) + ".txt"
    a()
    res = re.findall(r'原审|二审|再审', output)
    for item in res:
        if (item == '原审') | (item == '二审') | (item == '再审'):
            resname2 = path2 + str(name) + ".txt"
            if os.path.exists(resname2):
                os.remove(resname2)
            shutil.copyfile(fileName, resname2)
            return
    resname1 = path1 + str(name) + ".txt"
    if os.path.exists(resname1):
        os.remove(resname1)
    shutil.copyfile(fileName, resname1)



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
    labels = ['一审', '二审']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('审级信息柱状图')
    plt.ylim(0, 65)
    plt.show()


if __name__ == '__main__':
    while num <= 100:
        name = "%d" % num
        level()
        output = ''
        num = num + 1
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    print("一审：", total1)
    print("二审：", total2)
    b()
