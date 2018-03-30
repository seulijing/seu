# -*- coding:utf-8 -*-
import re
import shutil
import os
import matplotlib.pyplot as plt


filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\车牌\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\驾驶证\\'
path3 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\是否\\检查\\'
num = 1
total1 = 0
total2 = 0
total3 = 0


def ifw():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'伪造车牌|变造车牌|伪造驾驶证|变造驾驶证|逃避检查|拒绝检查|阻碍检查', sentence)
        for item in res:
            if (item == '伪造车牌') | (item == '变造车牌'):
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if (item == '伪造驾驶证') | (item == '变造驾驶证'):
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
            if (item == '逃避检查') | (item == '拒绝检查') | (item == '阻碍检查'):
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
    labels = ['车牌', '驾驶证', '检查']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('检查态度信息柱状图')
    plt.ylim(0, 15)
    plt.show()


if __name__ == '__main__':
    ifw()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path3):  # 遍历统计
        for each in files:
            total3 += 1  # 统计文件夹下文件个数
    print("车牌：", total1)
    print("驾驶证：", total2)
    print("检查：", total3)
