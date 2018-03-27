# -*- coding:utf-8 -*-
import os
import re
import shutil
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\审理程序\\简易程序\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\审理程序\\普通程序\\'
num = 1
total1 = 0
total2 = 0


def procedure():
    global num, total1, total2
    fileName = filepath + str(name) + ".txt"
    source = open(fileName, 'r')
    sentence = source.read()
    res = re.findall(r'简易程序', sentence)
    for item in res:
        if item == '简易程序':
            resname1 = path1 + str(name) + ".txt"
            if os.path.exists(resname1):
                os.remove(resname1)
            shutil.copyfile(fileName, resname1)
            total1 = total1 + 1
            return
    resname2 = path2 + str(name) + ".txt"
    if os.path.exists(resname2):
        os.remove(resname2)
    shutil.copyfile(fileName, resname2)
    total2 = total2 + 1
    source.close()


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['简易程序', '普通程序']
    p = plt.bar(range(len(data)), data, tick_label=labels)
    plt.title('审理程序信息柱状图')
    plt.ylim(0, 80)
    plt.show()


if __name__ == '__main__':
    while num <= 100:
        name = "%d" % num
        procedure()
        num = num + 1
    print("简易程序：", total1)
    print("普通程序：", total2)
    b()

