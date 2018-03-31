# -*- coding:utf-8 -*-
import re
import shutil
import os
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\严重后果\\重伤\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\严重后果\\死亡\\'
num = 1
total1 = 0
total2 = 0


def ifdie():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'重伤|当场死亡|无效死亡|而死亡|"损伤死亡', sentence)
        for item in res:
            if item == '重伤':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if (item == '当场死亡') | (item == '无效死亡') | (item == '而死亡') | (item == '损伤死亡'):
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['重伤', '死亡']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('伤亡信息柱状图')
    plt.ylim(0, 10)
    plt.show()


if __name__ == '__main__':
    ifdie()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    print("重伤：", total1)
    print("死亡：", total2)
    b()
