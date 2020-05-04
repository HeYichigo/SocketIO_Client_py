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

        接收数据需要调用 client.recv(channl,callback)

        callback 为收到消息时调用的方法，以下做了示例
'''
'''
    示例 channl ： collection_channl | view_channl

    发送到 collection_channl 的消息将转发至 view_channl 

    即 collection_channl 负责接收消息 view_channl 负责显示消息
'''

# 发送字符串


import client
client.send('collection_channl', 'please')
# 发送数字
client.send('collection_channl', 144)
# 发送对象
client.send('collection_channl', {'from': 'you', 'to': 'me', 'temp': 123})


def doSomeThing(*args):
    print('recv:', args)


# recv调用示例
client.recv('view_channl', doSomeThing)

# 若想收到消息 务必调用此方法
client.wait()
