# -*- coding:utf-8 -*-
import pymysql.cursors


# 数据库操作
config={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'qwerty12',
    'db':'B10',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor,
}
connection = pymysql.connect(**config)


def login(loginName):
    with connection.cursor() as cursor:
        sql="select user_id,login_pwd,user_type from user where login_name=%s"
        cursor.execute(sql,loginName)
        result=cursor.fetchone()
    return result
