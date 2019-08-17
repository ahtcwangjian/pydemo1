# -*- coding: utf-8 -*-
# @Author: wangjian
# @Date:   2019-08-17 09:57:51
# @Last Modified by:   wangjian
# @Last Modified time: 2019-08-17 10:29:40

import socket

#创建socket对象
s = socket.socket()
#将socket绑定到本机IP地址和端口
s.bind(('0.0.0.0',10001))
#服务器开始监听来自服务端的链接
s.listen()
while True:
	#每当接收到来自客户端socket的请求时，该方法就返回对应的socket 和 远程地址
	c,addr = s.accept()
	print(c)
	print('连接地址：',addr)
	c.send('服务器已经收到的你的消息'.encode('utf-8'))
	#关闭连接
	c.close()