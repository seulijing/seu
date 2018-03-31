# -*- coding:utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\地点\\'
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
total7 = 0


def loc():
    global num, total1, total2, total3, total4, total5, total6, total7
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
            res = re.findall(r'路口|街道|高速公路|城市干道|隧道|桥|交叉口', sentence)
            list1 = sorted(set(res), key=res.index)
            for item in list1:
                if item == '路口':
                    total1 = total1 + 1
                if item == '街道':
                    total2 = total2 + 1
                if item == '高速公路':
                    total3 = total3 + 1
                if item == '城市干道':
                    total4 = total4 + 1
                if item == '隧道':
                    total5 = total5 + 1
                if item == '桥':
                    total6 = total6 + 1
                if item == '交叉口':
                    total7 = total7 + 1
                result.write(item + ' ')
            source.close()
            result.close()
            print(num, list1)
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(5, 6))
    data = [total1, total2, total3, total4, total5, total6, total7]
    labels = ['路口', '街道', '高速公路', '城市干道', '隧道', '桥', '交叉口']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('地点信息柱状图')
    plt.ylim(0, 35)
    plt.show()


if __name__ == '__main__':
    loc()
    print("路口：", total1)
    print("街道：", total2)
    print("高速公路：", total3)
    print("城市干道：", total4)
    print("隧道：", total5)
    print("桥：", total6)
    print("交叉口：", total7)
    b()
