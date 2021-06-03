# *-* coding: utf-8 *-*
"""
作者：XGM
日期：2021.06.02 23:21:36
"""
# 服务端
import socket
import threading

con = threading.Condition() # 判断条件 锁

host = input('Input the servers IP address:')
post = 8888
data = ''
s = socket.socket()
print('Socket created')
s.bind((host,post))
s.listen(1) # 监听连接

print("Socket new listening")

def NotifyAll(sss):
    global data
    if con.acquire(): # 获取锁
        data = sss
        con.notifyAll() # 表示当前线程放弃对资源的占用，通知其他线程...
        con.release() # 释放锁

def threadOut(conn,nick): # 发送消息
    global data
    while True:
        if con.acquire():
            con.wait() # 放弃对当前资源的占用，等消息通知
            if data:
                try:
                    conn.send(data)
                    con.release()
                except:
                    con.release()
                    return
def threadIn(conn,nick):
    while True:
        try:
            temp = conn.recv(1024)
            if not temp:
                conn.close()
                return
            NotifyAll(temp)
            print(data)
        except:
            NotifyAll(nick+' '+'error')
            print(data)
            return



while True:
    conn,addr = s.accept()
    print('Connected with'+addr[0]+':'+str(addr[1]))
    nick = conn.recv(1024)
    nick = nick.decode()
    NotifyAll('Welcome'+' '+nick+' '+'to the rome')
    data = data.encode()
    conn.send(data)
    threading.Thread(target=threadOut,args=(conn,nick)).start()
    threading.Thread(target=threadIn,args=(conn,nick)).start()