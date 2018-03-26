# -*- coding:utf-8 -*-
import os  # 引入文件操作库

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\罚金\\'
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    if not os.path.getsize(fileName):  # 文件大小为0
        os.remove(fileName)  # 删除这个文件
    num = num + 1

