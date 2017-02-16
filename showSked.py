# -*- coding:utf-8 -*-
import pymysql.cursors

class show:
    showTime = ""
    performer = ""

    def __init__(self, performer, showTime):
        self.performer = performer
        self.showTime = showTime


# 数据库操作
config={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'Qwerty12',
    'db':'B10',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor,
}
connection = pymysql.connect(**config)
# # 执行sql语句

def insert(performer,showTime):
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，插入记录
            sql = 'INSERT INTO show_sked (performer, show_time) VALUES (%s, %s)'
            cursor.execute(sql, (performer,showTime))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close()


    # 执行sql语句
def select():

    with connection.cursor() as cursor:
            # 执行sql语句，进行查询
        sql = 'SELECT performer,show_id,show_time FROM show_sked '
        cursor.execute(sql)
            # 获取查询结果
        result = cursor.fetchall()
        print(result)
        for showInfo in result:
            showInfo['show_time']=str(showInfo['show_time'])       #对象格式转成str
        print(result)
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

    return result

def update():
    try:
        with connection.cursor() as cursor:
            sql='UPDATE show_sked SET performer=%s WHERE show_id=%s'
            cursor.execute(sql,('方大同','2'))
        connection.commit()
    finally:
        connection.close()

