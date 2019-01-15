# -*- coding: utf-8 -*-
# @Time    : 2019-01-14 21:10
# @Author  : luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : app.py
# @Software: PyCharm
import logging;logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

#定义服务器响应请求的的返回为 "Awesome Website"
@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    text = b'<h1>Awesome Website</h1>'
    return web.Response(body=text.encode('gbk'),content_type='text/html')

#建立服务器应用，并异步对首页"/"进行响应

def init():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)

init()