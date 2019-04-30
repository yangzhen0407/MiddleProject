# -*- encoding: utf-8 -*-
"""
    @version: python 3.7
    @time: 2019/4/25 20:26
    @author: YangZhen
    @editor: YangZhen
    @title: 系统程序入口，启动http服务
    @file: main.py
"""
from util.httpServer import HttpServer

if __name__ == '__main__':
    httpServer = HttpServer()
    httpServer.main()
