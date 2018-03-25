# -*- coding:utf-8 -*-
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'G:\stanford-corenlp-full-2018-02-27', lang='zh')
filename = 'C:\\Users\\Sylar\\Desktop\\SRTP\\demo\\1.txt'
source = open(filename, 'r')
sentence = source.read()
print(nlp.ner(sentence))
