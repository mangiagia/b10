# -*- coding:utf-8 -*-
import pymysql.cursors
import config

# class show:
#     showTime = ""
#     performer = ""
#
#     def __init__(self, performer, showTime):
#         self.performer = performer
#         self.showTime = showTime


connection = pymysql.connect(**config.sqlconfig)
# # 执行sql语句
# 插入演出数据
def insert(performer,showTime):

    with connection.cursor() as cursor:
            # 执行sql语句，插入记录
        sql = 'INSERT INTO show_sked (performer, show_time) VALUES (%s, %s)'
        cursor.execute(sql, (performer,showTime))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

# 修改演出数据
def update(performer,showTime,show_id):

    with connection.cursor() as cursor:
        sql = 'UPDATE show_sked SET performer=%s,show_time=%s WHERE show_id=%s'
        cursor.execute(sql, (performer,showTime,show_id))
    connection.commit()


# 查询演出列表
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

# 删除演出信息
def delete(show_id):

    with connection.cursor() as cursor:
        sql='DELETE FROM show_sked WHERE show_id=%s'
        cursor.execute(sql,(show_id))
    connection.commit()
