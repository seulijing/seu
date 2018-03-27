# -*- coding:utf-8 -*-
import re
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo1\\'
total1 = 0
total2 = 0
total3 = 0
total4 = 0
num = 1

def birthdate():
    global num, total1, total2, total3, total4
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        sentence = source.read()
        res = re.findall(r'\d{4}年\d{1,2}月\d{1,2}日出生', sentence)
        for item in res:
            result = re.findall(r'\d{4}年\d{1,2}月\d{1,2}日', item)
            for word in result:
                resl = re.findall(r'\d{4}', word)
                for w in resl:
                    age = 2018 - int(w)
                    if 18 <= age < 30:
                        total1 = total1 + 1
                    if 30 <= age < 40:
                        total2 = total2 + 1
                    if 40 <= age < 50:
                        total3 = total3 + 1
                    if age >= 50:
                        total4 = total4 + 1
        num = num + 1


if __name__ == '__main__':
    birthdate()
    print("18-29岁：", total1)
    print("30-39岁：", total2)
    print("40-49岁：", total3)
    print("50岁及以上：", total4)

