# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/25 20:34
    @author: YangZhen
    @editor：LiuTao
    @title: 配置数据库连接和操作
    @file: DBUtil.py
"""
import pymysql


class DBUtil:
    """
    数据库连接类，配置数据库的连接、关闭及查询修改操作
    """

    def __init__(self):
        self.db_conn = None  # 数据库连接对象
        self.db_cursor = None  # 游标对象

    def __open_conn(self):
        """
        获取数据库连接对象，并创建游标对象
        :return: 返回数据库连接对象
        """
        try:
            self.db_conn = pymysql.connect('localhost', 'root', '12345678', 'game')
            self.db_cursor = self.db_conn.cursor()
            print("Connected")
        except Exception as e:
            print("连接数据库错误")
            print(e)
        else:
            return self.db_conn

    def __close_conn(self):
        """
        关闭数据库连接,关闭游标
        :return: 关闭成功返回True，关闭失败返回False
        """
        try:
            self.db_cursor.close()
            self.db_conn.close()
        except Exception as e:
            print("关闭数据库错误")
            print(e)
        else:
            return self.db_conn

    def do_query(self, sql):
        """
        数据库查询操作(select)
        :param sql: 所要执行的sql语句
        :return: 返回查询到的数据
        """
        try:
            self.__open_conn()
            self.db_cursor.execute(sql)
            result = self.db_cursor.fetchall()
            self.__close_conn()
            return result
        except Exception as e:
            print("执行查询错误")
            print(e)

    def do_update(self, sql):
        """
        数据库更新操作（insert/delete/update）
        :param sql: 所要执行的sql语句
        :return: 返回查询到的数据
        """
        try:
            self.__open_conn()
            self.db_cursor.execute(sql)
            result = self.db_cursor.fetchall()
            self.__close_conn()
            return result
        except Exception as e:
            self.db_conn.rollback()
            print("执行更新错误")
            print(e)

if __name__ == '__main__':
    a = DBUtil()
    a.do_query("select * from user where name = '11' and password = md5('11')")

