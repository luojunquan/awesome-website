# -*- coding: utf-8 -*-
# @Time    : 2019-01-14 21:10
# @Author  : luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : app.py
# @Software: PyCharm
import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()

#定义服务器响应请求的的返回为 "Awesome Website"
@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    text = '这是首页'
    return web.Response(body=text.encode('gbk'),content_type='text/html')

@routes.get('/about')
async def about(request):
    await asyncio.sleep(0.5)
    return web.json_response({'name':'about','sex':'boy'},content_type='text/html')

#建立服务器应用，持续监听本地9000端口的http请求，并异步对首页"/"进行响应

def init():
    app = web.Application()
    app.add_routes(routes)
    logging.info('server started at http://127.0.0.1:8080...')
    web.run_app(app)


init()