import pymysql.cursors


# 公司电脑数据库连接
sqlconfig={
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'B10',
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor,
}

# ec2数据库连接
# sqlconfig={
#     'host':'127.0.0.1',
#     'port':3306,
#     'user':'root',
#     'password':'Qwerty12',
#     'db':'b10',
#     'charset':'utf8',
#     'cursorclass':pymysql.cursors.DictCursor,
# }
