"""
1、导入模块 socket
2、创建套接字，使用IPV4 UDP方式
3、数据的传递
4、关闭套接字
"""
# 1、导入模块 socket
import socket
# 2、创建套接字，使用IPV4 UDP方式
# socket.socket(协议类型，传输方式)
# 参数一：
# socket.AF_INET 使用IPV4
# socket.AF_INET6 使用IPV6
# 参数二：
# socket.SOCK_DGRAM 使用UDP的传输方式（无链接）
# socket.SOCK_STREAM 使用TCP的传输方式（有连接）
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、数据的传递
udp_socket.sendto("你好".encode(), ("192.168.0.142", 8888))
# 4、关闭套接字
udp_socket.close()

