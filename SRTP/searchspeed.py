# -*- coding:utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\分类\\追逐竞驶\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\速度\\'
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0


def speed():
    global num, total1, total2, total3, total4, total5
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        if os.path.exists(fileName):
            source = open(fileName, 'r')
            resName = path + str(name) + ".txt"
            if os.path.exists(resName):
                os.remove(resName)
            result = open(resName, 'w')
            sentence = source.read()
            res = re.findall(r'\d+(?:\.\d+)?km/h|\d+(?:\.\d+)?公里／小时|\d+(?:\.\d+)?km／h', sentence)
            list1 = sorted(set(res), key=res.index)
            for w in list1:
                ress = re.findall(r'\d+(?:\.\d+)?', w)
                for item in ress:
                    speed = float(item)
                    y = (speed-100)/100
                    if y < 0:
                        y = ((y*100+100)-60)/60
                        if y < 0:
                            y = ((y*60+60)-40)/40
                        if 0 < y < 0.1:
                            total1 = total1 + 1
                        if 0.1 <= y < 0.2:
                            total2 = total2 + 1
                        if 0.2 <= y < 0.3:
                            total3 = total3 + 1
                        if 0.3 <= y < 0.4:
                            total4 = total4 + 1
                        if y >= 0.4:
                            total5 = total5 + 1
                    print(num, y, '%')
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(6, 7))
    data = [total1, total2, total3, total4, total5]
    labels = ['0-10%', '10-20%', '20-30%', '30-40%', '40%以上']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width()/2, rect.get_height(), '%d' % int(rect.get_height()), ha='center', va='bottom')
    plt.title('超速信息柱状图')
    plt.ylim(0, 5)
    plt.show()


if __name__ == '__main__':
    speed()
    b()
