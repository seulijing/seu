# -*- coding:utf-8 -*-
import re
import os
filepath = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\'
path = 'C:\\Users\\Sylar\\Desktop\\SRTP\\提取\\罚金\\'
num = 1


def searchmoney():
    global num
    while num <= 100:
        name = "%d" % num
        fileName = filepath + str(name) + ".txt"
        source = open(fileName, 'r')
        resName = path + str(name) + ".txt"
        if os.path.exists(resName):
            os.remove(resName)
        result = open(resName, 'w')
        sentence = source.read()
        res = re.findall(r'\人民币.+\元|\罚金.+\元', sentence)
        CN_NUM={
            '〇': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '零': 0, '壹': 1, '贰': 2,
            '叁': 3, '肆': 4, '伍': 5, '陆': 6, '柒': 7, '捌': 8, '玖': 9,
        }
        CN_UNIT = {
            '十': 10,
            '拾': 10,
            '百': 100,
            '佰': 100,
            '千': 1000,
            '仟': 1000,
            '万': 10000,
            '萬': 10000,
            '亿': 100000000,
            '億': 100000000,
            '兆': 1000000000000,
        }

        def chinese_to_arabic(cn: str)-> int:
            #汉字转数字
            unit = 0  # current
            ldig = []  # digest
            for cndig in reversed(cn):
                if cndig in CN_UNIT:
                    unit = CN_UNIT.get(cndig)
                    if unit == 10000 or unit == 100000000:
                        ldig.append(unit)
                        unit = 1
                else:
                    dig = CN_NUM.get(cndig)
                    if unit:
                        dig *= unit
                        unit = 0
                    ldig.append(dig)
            if unit == 10:
                ldig.append(10)
            val, tmp = 0, 0
            for x in reversed(ldig):
                if x == 10000 or x == 100000000:
                    val += tmp * x
                    tmp = 0
                else:
                    tmp += x
            val += tmp
            return val
        for item in res:
            item1 = chinese_to_arabic(item)
            result.write(item1)
            result.write(' ')
        source.close()
        result.close()
    num = num + 1

