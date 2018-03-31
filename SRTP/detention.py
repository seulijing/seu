# -*- coding:utf-8 -*-
import os
import re
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
num = 1


def dete():
    global num, total1, total2, total3, total4, total5, total6
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'\拘役[一二三四五六七八九十]\个月', sentence)
        list1 = sorted(set(res), key=res.index)
        for item in list1:
            if item == "拘役一个月":
                total1 += 1
            if item == "拘役二个月":
                total2 += 1
            if item == "拘役三个月":
                total3 += 1
            if item == "拘役四个月":
                total4 += 1
            if item == "拘役五个月":
                total5 += 1
            if item == "拘役六个月":
                total6 += 1
        source.close()
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(6, 7))
    data = [total1, total2, total3, total4, total5, total6]
    labels = ['拘役一个月', '拘役二个月', '拘役三个月', '拘役四个月', '拘役五个月', '拘役六个月']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width()/2, rect.get_height(), '%d' % int(rect.get_height()), ha='center', va='bottom')
    plt.title('拘役信息柱状图')

    plt.ylim(0, 40)
    plt.show()


if __name__ == '__main__':
    dete()
    b()

