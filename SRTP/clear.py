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
    flag = 0
    for line in source.readlines():
        for seg in spy:
            if seg in line:
                flag = 1
                break
            if '原告' not in line:
                if '代理人' not in line:
                    result.write(line)
                    break
        if flag == 1:
            break
    source.close()
    result.close()
    num = num + 1
