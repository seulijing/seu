# -*- coding:utf-8 -*-
import os
import re
import shutil
import matplotlib.pyplot as plt

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\初级\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\中级\\'
path3 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\高级\\'
path4 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\法院级别\\最高\\'
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0


def searchcourt():
    global num
    global total1, total2, total3, total4
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence1 = source.readlines()[0]
        source.close()
        source = open(fileName, 'r')
        sentence2 = source.readlines()[1]
        sentence = sentence1 + sentence2
        res = re.findall(r'区人民法院|县人民法院|市人民法院|省人民法院|中级人民法院|初级人民法院|高级人民法院|最高人民法院', sentence)
        for item in res:
            if (item == '区人民法院') | (item == '县人民法院') | (item == '初级人民法院'):
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
                total1 = total1 + 1
            if (item == '市人民法院') | (item == '中级人民法院'):
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
                total2 = total2 + 1
            if (item == '省人民法院') | (item == '高级人民法院'):
                resname3 = path3 + str(name) + ".txt"
                if os.path.exists(resname3):
                    os.remove(resname3)
                shutil.copyfile(fileName, resname3)
                total3 = total3 + 1
            if (item == '最高人民法院'):
                resname4 = path4 + str(name) + ".txt"
                if os.path.exists(resname4):
                    os.remove(resname4)
                shutil.copyfile(fileName, resname4)
                total4 = total4 + 1
        num = num + 1
        source.close()


def b():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(figsize=(5, 6))
    data = [total1, total2, total3, total4]
    labels = ['初级人民法院', '中级人民法院', '高级人民法院', '最高人民法院']
    a = plt.bar(range(len(data)), data, tick_label=labels, color='#37C6C0')
    for rect in a:
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), '%d' % int(rect.get_height()), ha='center',
                 va='bottom')
    plt.title('法院级别信息柱状图')
    plt.ylim(0, 70)
    plt.show()


if __name__ == '__main__':
    searchcourt()
    print("初级人民法院：", total1)
    print("中级人民法院：", total2)
    print("高级人民法院：", total3)
    print("最高人民法院：", total4)
    b()
