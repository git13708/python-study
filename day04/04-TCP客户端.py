"""
1、导入模块
2、创建套接字 TCP
3、建立连接 connect()
4、发送数据
5、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字 TCP
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、建立连接 connect()
tcp_client_socket.connect(("192.168.0.142", 9990))
# 4、发送数据
tcp_client_socket.send("hello world".encode())
# 接收数据
recv_data = tcp_client_socket.recv(1024)
# 解码数据
recv_text = recv_data.decode(encoding="GBK", errors="ignore")
print("收到数据：%s" % recv_text)
# 5、关闭套接字
tcp_client_socket.close()
