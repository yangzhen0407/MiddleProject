# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:33
    @author: YangZhen
    @title: 所有SQL语句存放位置，二维字典形式存放
    @file: sql.py.py
"""
# 外层字典为："模块名":{}
# 内层字典为："sql语句名":"sql语句"
sql_dict = {
    "userDao": {
        "userLogin": "select * from user where user_name = %s user_password = md5(%s)"
    }

}
