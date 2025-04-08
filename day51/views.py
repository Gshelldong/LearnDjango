def index(env):
    return 'index'
def login(env):
    return 'login'
def errors(env):
    return '404 error'

def reg(env):
    return 'reg'

from datetime import datetime

def get_time(env):
    # 借助于时间模块 现在后端获取到时间数据
    current_time = datetime.now().strftime('%Y-%m-%d %X')
    with open(r'templates/02.get_time.html','r',encoding='utf-8') as f:
        data = f.read()  # data其实就是一串字符串  仅此而已!!!
    data = data.replace('$$time$$',current_time)
    return data


from jinja2 import Template
def get_user(env):
    user_dict = {'username':'jason','password':'123','hobby':['read','game','running']}
    with open(r'templates/03.get_user.html','r',encoding='utf-8') as f:
        data = f.read()
    temp = Template(data)
    res =  temp.render(data = user_dict)  # 将user_dict传递给前端页面 前端页面通过变量名data就能够获取到该字典
    return res

import pymysql
def get_db(env):
    # conn = pymysql.connect(
    #     host = '127.0.0.1',
    #     port = 3306,
    #     user = 'root',
    #     password = '123',
    #     database = 'day51',
    #     charset = 'utf8',
    #     autocommit = True
    # )
    # cursor = conn.cursor(pymysql.cursors.DictCursor)
    # sql = "select * from userinfo"
    # affect_rows = cursor.execute(sql)
    # data = cursor.fetchall()

    data = [{'id':1,'name':'john','password':'123'},
            {'id':2,'name':'tom','password':'tom@1122'},
            {'id':3,'name':'jerry','password':'abc123'},
            ]
    # print(data)
    with open(r'templates/04.get_db.html','r',encoding='utf-8') as f:
        data1 = f.read()
    temp = Template(data1)
    res = temp.render(user_list= data)
    return res

