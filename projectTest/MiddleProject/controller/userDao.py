# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:04
    @author: YangZhen
    @editor: ZhangBeiLe
    @title: 用户登录/注册/退出
    @file: userDao.py
"""
from util.db_util import DBUtil
from model.user import User
from util.sql import sql_dict
db_util=DBUtil()
class UserDao:
    def __init__(self):
        pass
    def get_user(self,user_msg):
        tmp = user_msg[1].split(' ')
        name = tmp[1]
        passwd = tmp[2]
        sql = 'select * from user_msg[0] where name="%s" and passwd="%s"' % (name, passwd)
        r=db_util.do_query(sql)
        if r:
            return True
        else:
            return False
    def reg(self,user):
        L = user.split(' ')
        name = L[1]
        passwd = L[2]
        sql = "select * from user where name='%s'" % name
        r =db_util.do_query(sql)
        if r != None:
            return False
        else:
            sql = "insert into user (name,passwd) values ('%s','%s')" % (name, passwd)
            db_util.do_update(sql)
            return True

    def log(self,user_name,user_passwd):
        name = user_name
        passwd = user_passwd
        sql = 'select * from user where name="%s" and passwd="%s"' % (name, passwd)
        r = db_util.do_query(sql)
        if r:
            return user_name,user_passwd
        else:
            return self.log()
