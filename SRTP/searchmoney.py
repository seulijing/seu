# -*- coding:utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\罚金\\'
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0
total8 = 0
total9 = 0


def searchmoney():
    global num, total1, total2, total3, total4, total5, total6, total7, total8, total9
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        resName = path + str(name) + ".txt"
        if os.path.exists(resName):
            os.remove(resName)
        result = open(resName, 'w')
        sentence = source.read()
        res = re.findall(r'\罚金[一二三四五六七八九]+?\千元|\罚金人民币[一二三四五六七八九]+?\千元', sentence)
        list1 = sorted(set(res), key=res.index)
        for w in list1:
            ress = re.findall(r'[一二三四五六七八九]+?\千元', w)
            for item in ress:
                if item == "一千元":
                    total1 += 1
                if item == "二千元":
                    total2 += 1
                if item == "三千元":
                    total3 += 1
                if item == "四千元":
                    total4 += 1
                if item == "五千元":
                    total5 += 1
                if item == "六千元":
                    total6 += 1
                if item == "七千元":
                    total7 += 1
                if item == "八千元":
                    total8 += 1
                if item == "九千元":
                    total9 += 1
        source.close()
        result.close()
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(6, 7))
    data = [total1, total2, total3, total4, total5, total6, total7, total8, total9]
    labels = ['一千元', '二千元', '三千元', '四千元', '五千元', '六千元', '七千元', '八千元', '九千元']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width()/2, rect.get_height(), '%d' % int(rect.get_height()), ha='center', va='bottom')
    plt.title('罚金信息柱状图')
    plt.ylim(0, 25)
    plt.show()


if __name__ == '__main__':
    searchmoney()
    b()
