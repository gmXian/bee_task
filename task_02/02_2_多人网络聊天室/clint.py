# *-* coding: utf-8 *-*
"""
作者：XGM
日期：2021.06.02 21:59:11
"""
# 客户端
import socket
import threading

outString = ''
nick = ''
inString = ''
def clint_send(sock):
    global outString
    while True: # 让客户端一直能处于发送状态
        outString = input() # 接受输入
        outString = nick+':'+outString
        outString = outString.encode()
        sock.send(outString)

def client_accept(sock):
    global inString
    while True:
        try:
            inString = sock.recv(1024) #接收数据
            if not inString:
                break
            if outString != inString:
                print(inString.decode("utf8"))
        except:
            break


nick = input("input your nickname:")

ip = input("input the server ip address:")
port = 8888 #端口
sock = socket.socket() # 创建套接字(??)
sock.connect((ip,port)) # 连接
nick = nick.encode()
sock.send(nick) # 把用户名发送给服务端
nick = nick.decode()
# 启动两个线程，一个用于接收消息，一个用于发送消息

th_send = threading.Thread(target=clint_send,args=(sock,)) # 用于发送消息
th_send.start()
th_accept = threading.Thread(target=client_accept,args=(sock,)) # 用于接受消息
th_accept.start()



