# -*- coding:utf-8 -*-
import os
import re
import shutil
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\大学\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\小学\\'
path3 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\初中\\'
path4 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\高中\\'
path5 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\中专\\'
path6 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\硕士\\'
path7 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\专科\\'
path8 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\大专\\'
path9 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\学历\\技校\\'
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


def education():
    global num, total1, total2, total3, total4, total5, total6, total7, total8, total9
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'，大学|，小学|，初中|，高中|中专|大专|硕士|专科|，技校', sentence)
        for item in res:
            if item == '，大学':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
                total1 = total1 + 1
            if item == '，小学':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
                total2 = total2 + 1
            if item == '，初中':
                resname3 = path3 + str(name) + ".txt"
                if os.path.exists(resname3):
                    os.remove(resname3)
                shutil.copyfile(fileName, resname3)
                total3 = total3 + 1
            if item == '，高中':
                resname4 = path4 + str(name) + ".txt"
                if os.path.exists(resname4):
                    os.remove(resname4)
                shutil.copyfile(fileName, resname4)
                total4 = total4 + 1
            if item == '中专':
                resname5 = path5 + str(name) + ".txt"
                if os.path.exists(resname5):
                    os.remove(resname5)
                shutil.copyfile(fileName, resname5)
                total5 = total5 + 1
            if item == '硕士':
                resname6 = path6 + str(name) + ".txt"
                if os.path.exists(resname6):
                    os.remove(resname6)
                shutil.copyfile(fileName, resname6)
                total6 = total6 + 1
            if item == '专科':
                resname7 = path7 + str(name) + ".txt"
                if os.path.exists(resname7):
                    os.remove(resname7)
                shutil.copyfile(fileName, resname7)
                total7 = total7 + 1
            if item == '大专':
                resname8 = path8 + str(name) + ".txt"
                if os.path.exists(resname8):
                    os.remove(resname8)
                shutil.copyfile(fileName, resname8)
                total8 = total8 + 1
            if item == '，技校':
                resname9 = path9 + str(name) + ".txt"
                if os.path.exists(resname9):
                    os.remove(resname9)
                shutil.copyfile(fileName, resname9)
                total9 = total9 + 1
        num = num + 1


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(3, 5))
    data = [total1, total2]
    labels = ['男', '女']
    plt.bar(range(len(data)), data, tick_label=labels)
    plt.title('被告人性别信息柱状图')
    plt.ylim(0, 80)
    plt.show()


if __name__ == '__main__':
    education()
    print("大学：", total1)
    print("小学：", total2)
    print("初中：", total3)
    print("高中：", total4)
    print("中专：", total5)
    print("硕士：", total6)
    print("专科：", total7)
    print("大专：", total8)
    print("技校：", total9)

