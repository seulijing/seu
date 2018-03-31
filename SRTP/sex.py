# -*- coding:utf-8 -*-
import os
import re
import shutil
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告性别\\男\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\被告性别\\女\\'
num = 1
total1 = 0
total2 = 0


def sex():
    global num, total1, total2
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'，男，|，女，', sentence)
        for item in res:
            if item == '，男，':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
                total1 = total1 + 1
            if item == '，女，':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
                total2 = total2 + 1
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['男', '女']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('被告人性别信息柱状图')
    plt.ylim(0, 80)
    plt.show()


if __name__ == '__main__':
    sex()
    print("男：", total1)
    print("女：", total2)
    b()
