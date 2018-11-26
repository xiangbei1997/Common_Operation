# 这样只能实现传送一次数据
"""import socket

# 创建socket连接
client  = socket.socket()

# 选择连接地址和端口
client.connect(('localhost',9998))

# 发送数据
client.send(b'hello,world')

# 关闭连接
client.close() """

# 单人发送多次数据
"""
import socket

local_port = ('localhost',9998)

# 创建socket连接
client = socket.socket()

# 选择连接地址和端口
client.connect(local_port)

while True:
    direct = input('>>请问您有什么指示：')
    if len(direct) == 0 : break
    client.send(bytes(direct.encode('utf-8')))
    data =  client.recv(1024)
    print(str(data))

client.close() """

# 多人通信
"""
import socket

local_port = ('localhost',9998)

# 创建socket连接
client = socket.socket()

# 选择连接地址和端口
client.connect(local_port)

while True:
    direct = input('>>请问您有什么指示：')
    if len(direct) == 0 : break
    client.send(bytes(direct.encode('utf-8')))
    data =  client.recv(1024)
    print(str(data))

client.close() """

# 实现简单的shh
"""
import socket

client = socket.socket()

client.connect(("localhost",9998))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    data = client.recv(1024)
    print(data.decode()) #命令执行结果

client.close() """

# 实现大量shh大量数据的获取数据
"""第一次获取到的是一个数据大小的值，获取到这个值后，我们来确定这里命令执行后产生多少数据。用我们的reve接受全部server发送的数据"""
"""
import socket
import sys

client = socket.socket()

client.connect(("localhost",9999))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8") )

    res_return_size  = client.recv(1024) #接收这条命令执行结果的大小
    print("getting cmd result , ", res_return_size)
    total_rece_size = int(res_return_size)
    print("total size:",res_return_size)
    client.send("准备好接收了,发吧loser".encode("utf-8"))
    received_size = 0 #已接收到的数据
    cmd_res = b''
    f = open("test_copy.html","wb")#把接收到的结果存下来,一会看看收到的数据 对不对
    while received_size != total_rece_size: #代表还没收完
        data = client.recv(1024)
        received_size += len(data) #为什么不是直接1024,还判断len干嘛,注意,实际收到的data有可能比1024少
        cmd_res += data
    else:
        print("数据收完了",received_size)
        #print(cmd_res.decode())
        f.write(cmd_res) #把接收到的结果存下来,一会看看收到的数据 对不对
    #print(data.decode()) #命令执行结果

client.close() """