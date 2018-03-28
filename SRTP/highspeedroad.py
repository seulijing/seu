# -*- coding:utf-8 -*-
import re
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
path1 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\道路\\高速公路\\'
path2 = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\道路\\城市快速路\\'
num = 1
total1 = 0
total2 = 0


def road():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'高速公路|城市快速路', sentence)
        for item in res:
            if item == '高速公路':
                resname1 = path1 + str(name) + ".txt"
                if os.path.exists(resname1):
                    os.remove(resname1)
                shutil.copyfile(fileName, resname1)
            if item == '城市快速路':
                resname2 = path2 + str(name) + ".txt"
                if os.path.exists(resname2):
                    os.remove(resname2)
                shutil.copyfile(fileName, resname2)
        num = num + 1


if __name__ == '__main__':
    road()
    for root, dirs, files in os.walk(path1):  # 遍历统计
        for each in files:
            total1 += 1  # 统计文件夹下文件个数
    for root, dirs, files in os.walk(path2):  # 遍历统计
        for each in files:
            total2 += 1  # 统计文件夹下文件个数
    print("高速公路：", total1)
    print("城市快速路：", total2)
