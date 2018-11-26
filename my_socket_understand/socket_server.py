# 这样只能实现传送一次数据，最简单的socket连接
"""import socket
# 获取socket实力
server = socket.socket()

# 绑定本机IP端口，这里不写就是默认本地
server.bind(('',9998))

# 开始监听
server.listen(5)

# 接受并建立连接，程序在此开始阻塞，知道有客户端连接进来,第一个参数是接受的内容，第二是连接客户的地址
conn,adders = server.accept()
print('%s-已经连接到本服务器',adders)

# 拿到接受信息，获取1024个字节
data = conn.recv(1024)
print(data)

# 关闭连接
server.close() """

# 实现多次传送数据交互
"""
# 实现一个简易的两人通信系统
import socket

local_port = ('',9998)
# 创建socket对象
server  = socket.socket()

# 绑定本机
server.bind(local_port)

# 开始监听
server.listen(5)

# 接受监听并创建连接，程序开始阻塞，直到有客户连接进来
conn,adders = server.accept()

while True:
    data = conn.recv(1024)
    print(str(data))
    if not data:
        print('交互完成')
        break
    send_data = input('>>回复')
    conn.send(bytes(send_data.encode('utf-8')))

server.close() """

# 实现多人通信
"""
# 实现多人通信

import socket
server =socket.socket()

local_port = ('',9998)
server.bind(local_port)
server.listen()
while True:
    conn, adders = server.accept()
    print('连接的地址%s', adders)
    while True:
       data = conn.recv(1024)
       if data == 0 : break
       print('接受的内容%s',data)
       send= input(">>:")
       conn.send(bytes(send.encode('utf-8')))

server.close() """

# 实现简单的shh
"""
import socket
import os


server = socket.socket() #获得socket实例
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9998)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("收到命令:",data)
        res = os.popen(data.decode()).read() #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
        print(len(res))
        conn.send(res.encode("utf-8"))

server.close() """

# 实现每次发送大量数据，客户端每次都可以接收到。
"""第一次获取到客户端执行的命令我们这边需要执行完成后由多大的数据，第二次在发送具体的数据"""
"""
import socket
import os,subprocess


server = socket.socket() #获得socket实例
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9999)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("收到命令:",data)
        #res = os.popen(data.decode()).read() #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下
        res = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE).stdout.read() #跟上面那条命令的效果是一样的
        if len(res) == 0:
            res = "cmd exec success,has not output!".encode("utf-8")
        conn.send(str(len(res)).encode("utf-8")) #发送数据之前,先告诉客户端要发多少数据给它
        print("等待客户ack应答...")
        client_final_ack = conn.recv(1024) #等待客户端响应
        print("客户应答:",client_final_ack.decode())
        print(type(res))
        conn.sendall(res) #发送端也有最大数据量限制,所以这里用sendall,相当于重复循环调用conn.send,直至数据发送完毕
 
server.close() """