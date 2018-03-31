# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
import matplotlib.pyplot as plt
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0


def time():
    global num, total1, total2, total3, total4
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        if os.path.exists(fileName):
            source = open(fileName, 'r')
            sentence = source.read()
            res = re.findall(r'\d+(?:\.\d+)?时', sentence)
            list1 = sorted(set(res), key=res.index)

            def aa():
                global total1, total2, total3, total4
                for a in list1:
                    ress = re.findall(r'\d{1,2}', a)
                    for w in ress:
                        time = int(w)
                        if 0 <= time < 8:
                            total1 = total1 + 1
                            return
                        if 8 <= time < 12:
                            total2 = total2 + 1
                            return
                        if 12 <= time < 19:
                            total3 = total3 + 1
                            return
                        if 19 <= time < 24:
                            total4 = total4 + 1
                            return
            aa()
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(5, 6))
    data = [total1, total2, total3, total4]
    labels = ['0-8时', '8-12时', '12-19时', '19-24时']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width()/2, rect.get_height(), '%d' % int(rect.get_height()), ha='center', va='bottom')
    plt.title('时间信息柱状图')

    plt.ylim(0, 55)
    plt.show()


if __name__ == '__main__':
    time()
    b()
