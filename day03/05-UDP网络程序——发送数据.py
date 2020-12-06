"""
1、导入模块
2、创建套接字
3、发送数据
4、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、发送数据
# 参数一：
# 需要发送的数据
# 参数二：
# 对方的IP和端口号
udp_socket.sendto("你好".encode(), ("192.168.0.142", 8888))
# 4、关闭套接字
udp_socket.close()
