# -*- coding:utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\车辆型号\\'
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0


def vm():
    global num
    global total1, total2, total3, total4, total5, total6
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
            res = re.findall(r'面包车|校车|汽车|客车|摩托|轿车', sentence)
            list1 = sorted(set(res), key=res.index)
            for item in list1:
                if item == "面包车":
                    total1 += 1
                if item == "校车":
                    total2 += 1
                if item == "汽车":
                    total3 += 1
                if item == "客车":
                    total4 += 1
                if item == "摩托":
                    total5 += 1
                if item == "轿车":
                    total6 += 1
                result.write(item + ' ')
            source.close()
            result.close()
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(5, 6))
    data = [total1, total2, total3, total4, total5, total6]
    labels = ['面包车', '校车', '汽车', '客车', '摩托', '轿车']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('车辆信息柱状图')
    plt.ylim(0, 60)
    plt.show()


if __name__ == '__main__':
    vm()
    print('面包车', total1)
    print('校车', total2)
    print('汽车', total3)
    print('客车', total4)
    print('摩托', total5)
    print('轿车', total6)
    b()
