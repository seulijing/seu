# -*- coding:utf-8 -*-
import re
import shutil
import os

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
