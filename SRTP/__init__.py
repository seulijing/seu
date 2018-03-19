# -*- coding:utf-8 -*-
import codecs
import os
import shutil
import jieba


# Read file and cut
def read_file_cut():
    # create path
    path = "C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\"
    respath = "C:\\Users\\Sylar\\Desktop\\SRTP\\result\\"
    if os.path.isdir(respath):
        shutil.rmtree(respath, True)
    os.makedirs(respath)
    jieba.load_userdict("dict.txt")  # 导入用户自定义词典
    num = 1
    while num <= 100:
        name = "%d" % num
        fileName = path + str(name) + ".txt"
        resName = respath + str(name) + ".txt"
        source = open(fileName, 'r')
        if os.path.exists(resName):
            os.remove(resName)
        result = open(resName, 'w')
        stopwords = {}.fromkeys([line.strip() for line in codecs.open('stopwords.txt')])   # 停用词表
        for line in source:
            seglist = jieba.cut(line)
            output = ''
            for segs in seglist:
                seg = segs.lower()  # 英文字母小写
                if seg not in stopwords:  # 去停用词

                    output += seg
                    output += ' '
            result.write(output)
        else:
            print('End file: ' + str(num))
            source.close()
            result.close()
        num = num + 1
    else:
        print('End All')


if __name__ == '__main__':
    read_file_cut()
