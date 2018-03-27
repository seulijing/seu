import shutil
import os

filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
if os.path.isdir(path):
    shutil.rmtree(path, True)
os.makedirs(path)
num = 1
while num <= 100:
    name = "%d" % num
    fileName = filepath + str(name) + ".txt"
    resname = path + str(name) + ".txt"
    source = open(fileName, 'r')
    result = open(resname, 'w')
    for line in source.readlines():
        if '原告' not in line:
            if '代理人' not in line:
                result.write(line)
    source.close()
    result.close()
    num = num + 1
