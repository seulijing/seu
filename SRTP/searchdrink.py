# -*- coding:utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\分类\\醉驾\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\酒精浓度\\'
num = 1
total1 = 0
total2 = 0
def drink():
    global num, total1, total2
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
            res = re.findall(r'\d+(?:\.\d+)?mg/|\d+(?:\.\d+)?mg／|\每百毫升.+\毫克|\d+(?:\.\d+)?mg／ml|\d+(?:\.\d+)?mg/|'
                             r'\d+(?:\.\d+)?mg（乙醇）／ml（血液）|\d+(?:\.\d+)?mg／|\d+(?:\.\d+)?毫克/|\d+(?:\.\d+)?mg/dl|'
                             r'\d+(?:\.\d+)?毫克／毫升|\d+(?:\.\d+)?mg/|\毫升血液中酒精含量为.+\毫克', sentence)
            list1 = sorted(set(res), key=res.index)
            for item in list1:
                res1 = re.findall(r'\d+(?:\.\d+)?', item)
                for a in res1:
                    n = float(a)
                    if (n != 80.0) & (n != 200.0):
                        if n < 10:
                            n = n * 100
                        numb = round(n, 1)
                        if 80 < numb < 200:
                            total1 = total1 + 1
                        if numb >= 200:
                            total2 = total2 + 1
                        print(num, numb)
            source.close()
            result.close()
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['80-200mg/100ml', '200mg/100ml以上']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('酒精信息柱状图')
    plt.ylim(0, 80)
    plt.show()


if __name__ == '__main__':
    drink()
    print("一般醉驾：", total1)
    print("从重：", total2)
    b()