import codecs
import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    resname = path + str(name) + ".txt"
    source = open(fileName, 'r')
    result = open(resname, 'w')
    spy = {}.fromkeys([line.strip() for line in codecs.open('spy.txt')])
    for line in source.readlines():
        if '审判员' in line or '审判长' in line or '代书记员' in line or '书记员' in line or '附件' in line or '附相关法条' in line or '陪审员' in line or '人民陪审员' in line:
            break
        if '原告' not in line and '代理人' not in line:
            result.write(line)

    source.close()
    result.close()
    num = num + 1
