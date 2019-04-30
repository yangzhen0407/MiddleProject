# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/30 22:09
    @author: YangZhen
    @editor: YangZhen
    @title: 移动点实体类
    @file: vector.py
"""


class Vector:
    """
    移动点坐标，x:行 y:列
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
