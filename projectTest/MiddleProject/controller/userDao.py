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

db_util = DBUtil()


class UserDao:
    def __init__(self):
        pass

    def get_user(self, user_msg: dict):
        """
        根据指定信息查询是否存在该用户
        :param user_msg: 字典形式，{"数据库列名":"值"}
        :return: 查询结果不为空返回True，查询失败返回False
        """
        pass

    def reg(self, user: User):
        """
        用户注册
        :param user: 用户信息
        :return: 注册成功返回True,注册失败返回False
        """
        pass

    def log(self, user_name, user_passwd) -> User:
        """
        用户登录
        :param user_name: 用户名
        :param user_passwd: 密码
        :return: 返回查询到的用户信息
        """
        pass
