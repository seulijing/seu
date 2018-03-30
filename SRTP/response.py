# -*- coding:utf-8 -*-
import re
import shutil
import os
import matplotlib.pyplot as plt
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\责任\\主要责任\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\责任\\同等责任\\'
path3 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\责任\\次要责任\\'
num = 1
total1 = 0
total2 = 0
total3 = 0


def response():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'主要责任|同等责任|次要责任', sentence)
        for item in res:
            if item == '主要责任':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if item == '同等责任':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
            if item == '次要责任':
                resname3 = path3 + str(name) + ".txt"
                if os.path.exists(resname3):
                    os.remove(resname3)
                shutil.copyfile(fileName, resname3)
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(5, 6))
    data = [total1, total2, total3]
    labels = ['主要责任', '同等责任', '次要责任']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('责任信息柱状图')
    plt.ylim(0, 15)
    plt.show()


if __name__ == '__main__':
    response()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path3):  # 遍历统计
        for each in files:
            total3 += 1  # 统计文件夹下文件个数
    print("主要责任：", total1)
    print("同等责任：", total2)
    print("次要责任：", total3)
    b()
