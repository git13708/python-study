"""
1、导入模块
2、创建套接字
3、发送数据
4、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、发送数据
# 4、关闭套接字
tcp_socket.close()
