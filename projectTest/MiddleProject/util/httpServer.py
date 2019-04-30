# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/25 20:49
    @author: YangZhen
    @editor: FanShanShan
    @title: http服务端
    @file: httpServer.py
"""
from util.config import *

ADDRESS = (NETHOST, PORT)


class HttpServer:
    """
        http服务器，循环等待客户端连接
    """

    def __init__(self):
        pass

    def handle(self):
        """
        处理客户端请求
        :return:
        """
        pass

    def response(self):
        """
        将数据组织称http响应格式发送给浏览器
        :return:
        """
        pass

    def main(self):
        """
        启动http服务器
        :return: 无返回值
        """
        pass
