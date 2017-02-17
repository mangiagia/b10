# -*- coding:utf-8 -*-
import pymysql.cursors
import config


connection = pymysql.connect(**config.sqlconfig)


def login(loginName):
    with connection.cursor() as cursor:
        sql="select user_id,login_pwd,user_type from user where login_name=%s"
        cursor.execute(sql,loginName)
        result=cursor.fetchone()
    return result
