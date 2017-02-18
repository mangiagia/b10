# -*- coding:utf-8 -*-
import pymysql.cursors
import config

class volunteer:
    name = ""
    mobile = ""
    volunteer_type =""
    is_food = ""
    is_volunteer =""
    remark =""
    created_date=""

connection = pymysql.connect(**config.sqlconfig)
# # 执行sql语句

def insert(name,show_id,mobile,volunteer_type,is_food,is_volunteer,remark,created_date):

    with connection.cursor() as cursor:
            # 执行sql语句，插入记录
        sql = 'INSERT INTO volunteer (name,show_id,mobile,volunteer_type,is_food,is_volunteer,remark,created_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) '
        cursor.execute(sql, (name,show_id,mobile,volunteer_type,is_food,is_volunteer,remark,created_date))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()


#查询志愿者
def select(show_id):

    with connection.cursor() as cursor:
            # 执行sql语句，进行查询
        sql = 'SELECT id,name,mobile,volunteer_type,is_food,is_volunteer,remark FROM volunteer WHERE show_id=%s'
        cursor.execute(sql, (show_id))
            # 获取查询结果
        result = cursor.fetchall()
        print(result)


        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()

    return result



# 设置志愿者状态
def update(id,is_volunteer):

    with connection.cursor() as cursor:
        sql='UPDATE volunteer SET is_volunteer=%s WHERE id=%s'
        cursor.execute(sql,(is_volunteer,id))
    connection.commit()