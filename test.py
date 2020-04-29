# coding: utf-8
'''
    本文件为示例程序
    
    说明：

        使用之前安装socketIO-client
            $ pip install socketIO-client

        与服务端的连接在 client.py 中完成

    使用 client.py 进行开发：

        首先将 client.py 文件放在项目目录下

        执行 import client

        发送数据只需调用 client.send() 即可
'''
import client

# 发送字符串
client.send('please')
# 发送数字
client.send(144)
# 发送对象
client.send({'from': 'you', 'to': 'me', 'temp': 123})
