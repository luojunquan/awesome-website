#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:04
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : orm.py
# @Software: PyCharm
import asyncio,logging,aiomysql

def log(sql,args=()):
    logging.info('SQL:%s' % sql)

async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )