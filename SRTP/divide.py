# -*- coding:utf-8 -*-
import codecs
import os
import shutil
import jieba
import jieba.analyse
from matplotlib import pyplot as plt

textrank = jieba.analyse.textrank
# Read file and cut
num = 1
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
output = ''
path = "C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\"
respath1 = "C:\\Users\\Sylar\\Desktop\\SRTP\\醉驾\\"
respath2 = "C:\\Users\\Sylar\\Desktop\\SRTP\\追逐竞驶\\"
respath3 = "C:\\Users\\Sylar\\Desktop\\SRTP\\危险化学品\\"
respath4 = "C:\\Users\\Sylar\\Desktop\\SRTP\\客车校车\\"
respath5 = "C:\\Users\\Sylar\\Desktop\\SRTP\\混合\\"


def read_file_cut():
    # create path
    if os.path.isdir(respath1):
        shutil.rmtree(respath1, True)
    os.makedirs(respath1)
    if os.path.isdir(respath2):
        shutil.rmtree(respath2, True)
    os.makedirs(respath2)
    if os.path.isdir(respath3):
        shutil.rmtree(respath3, True)
    os.makedirs(respath3)
    if os.path.isdir(respath4):
        shutil.rmtree(respath4, True)
    os.makedirs(respath4)
    if os.path.isdir(respath5):
        shutil.rmtree(respath5, True)
    os.makedirs(respath5)
    jieba.load_userdict("dict.txt")  # 导入用户自定义词典
    global num
    global output
    global count1, count2, count3, count4
    global total1, total2, total3, total4, total5
    while num <= 100:
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        name = "%d" % num
        fileName = path + str(name) + ".txt"
        source = open(fileName, 'r')
        dwords1 = {}.fromkeys([line.strip() for line in codecs.open('dwords1.txt')])
        dwords2 = {}.fromkeys([line.strip() for line in codecs.open('dwords2.txt')])
        dwords3 = {}.fromkeys([line.strip() for line in codecs.open('dwords3.txt')])
        dwords4 = {}.fromkeys([line.strip() for line in codecs.open('dwords4.txt')])
        a()
        for word in output.split():
            if word in dwords1:
                count1 = count1 + 1
            if word in dwords2:
                count2 = count2 + 1
            if word in dwords3:
                count3 = count3 + 1
            if word in dwords4:
                count4 = count4 + 1
        if (count1 / (count1 + count2 + count3 + count4)) >= 0.8:
            resName1 = respath1 + str(name) + ".txt"
            if os.path.exists(resName1):
                os.remove(resName1)
            shutil.copyfile(fileName, resName1)
            total1 = total1 + 1
        if (count2 / (count1 + count2 + count3 + count4)) >= 0.8:
            resName2 = respath2 + str(name) + ".txt"
            if os.path.exists(resName2):
                os.remove(resName2)
            shutil.copyfile(fileName, resName2)
            total2 = total2 + 1
        if (count3 / (count1 + count2 + count3 + count4)) >= 0.8:
            resName3 = respath3 + str(name) + ".txt"
            if os.path.exists(resName3):
                os.remove(resName3)
            shutil.copyfile(fileName, resName3)
            total3 = total3 + 1
        if (count4 / (count1 + count2 + count3 + count4)) >= 0.8:
            resName4 = respath4 + str(name) + ".txt"
            if os.path.exists(resName4):
                os.remove(resName4)
            shutil.copyfile(fileName, resName4)
            total4 = total4 + 1
        if (((count1 / (count1 + count2 + count3 + count4)) >= 0.2) + (
                (count2 / (count1 + count2 + count3 + count4)) >= 0.2) + (
                    (count3 / (count1 + count2 + count3 + count4)) >= 0.2) + (
                    (count4 / (count1 + count2 + count3 + count4)) >= 0.2)) >= 2:
            resName5 = respath5 + str(name) + ".txt"
            if os.path.exists(resName5):
                os.remove(resName5)
            shutil.copyfile(fileName, resName5)
            total5 = total5 + 1
        num = num + 1
        output = ''
        source.close()
    else:
        print('End All')


def a():
    global num
    global output
    name = "%d" % num
    fileName = path + str(name) + ".txt"
    source = open(fileName, 'r')
    dwords = {}.fromkeys([line.strip() for line in codecs.open('dwords.txt')])
    spy = {}.fromkeys([line.strip() for line in codecs.open('spy.txt')])
    for line in source:
        seglist = jieba.cut(line)
        for segs in seglist:
            if segs not in spy:
                seg = segs.lower()
                if seg in dwords:
                    output += seg
                    output += ' '
            else:
                return


def b():

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    #  调节图形大小，宽，高
    plt.figure(figsize=(6, 9))
    # 定义饼状图的标签，标签是列表
    labels = [u'醉驾', u'追逐竞驶', u'危险化学品', u'客车校车', u'混合']
    # 每个标签占多大，会自动去算百分比
    sizes = [total1, total2, total3, total4, total5]
    colors = ['red', 'yellowgreen', 'lightskyblue', 'green', 'blue']
    # 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    patches, l_text, p_text = plt.pie(sizes, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.8)
    plt.title('危险驾驶罪分类信息饼状图')
    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for t in l_text:
        t.set_size = (30)
    for t in p_text:
        t.set_size = (20)
    # 设置x，y轴刻度一致，这样饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    read_file_cut()
    print("醉驾：", total1)
    print("追逐竞驶：", total2)
    print("危险化学品：", total3)
    print("客车校车：", total4)
    print("混合：", total5)
    b()
