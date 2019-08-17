# -*- coding: utf-8 -*-
# @Author: wangjian
# @Date:   2019-08-17 10:05:21
# @Last Modified by:   wangjian
# @Last Modified time: 2019-08-17 11:30:01

import socket

#创建socket对象
s = socket.socket()

#连接远程服务器
s.connect(('127.0.0.1',10001))
print(s.recv(1024).decode('utf-8'))
s.close()