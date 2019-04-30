# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:01
    @author: YangZhen
    @editor：LiJiaHe/GaoJiaYang
    @title: 处理用户移动操作
    @file: gameController.py
"""


class UserDao:
    def __init__(self, num_list, vector):
        """
        构造方法
        :param num_list: 待移动列表
        :param vector: 移动点坐标
        """
        self.num_list = num_list
        self.vector = vector

    def remove(self):
        """
        消除操作(LiJiaHe)
        :return:
        """
        self.__remove_row()
        self.__remove_col()

    def can_remove(self):
        """
        判断列表是否可以消除
        :return: 可以消除返回True，不可以消除返回False
        """
        pass

    def __remove_row(self):
        """
        游戏列表行消除操作(LiJiaHe)
        :return:
        """
        pass

    def __remove_col(self):
        """
        游戏列表列消除操作
        :return:
        """
