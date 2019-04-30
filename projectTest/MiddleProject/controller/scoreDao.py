# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:53
    @author: YangZhen
    @editor: ChenJianQiao
    @title: 用户移动后生成积分，并将积分保存到数据库中
    @file: scoreDao.py
"""
from util.db_util import DBUtil
from util.sql import sql_dict


class ScoreDao:
    def __init__(self, user_id):
        self.user_id = user_id

    def save_score(self, score):
        """
        将分数持久化到数据库中
        :param score: 分数
        :return: 保存成功返回True，保存失败返回False
        """
        pass
