# -*- coding:utf-8 -*-
import pymysql
db = pymysql.connect("localhost", "root", "1234", "srtp")
db.close()
