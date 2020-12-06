"""
1、导入模块
2、创建套接字
3、绑定端口
4、发送数据
5、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、绑定端口
# udp_socket.bind(address)
# address是一个元组，元组的第一个元素是字符串类型的IP地址，第二个元素 整数端口号
udp_socket.bind(("192.168.0.117", 8888))
# 4、发送数据
udp_socket.sendto("hello world".encode(), ("192.168.0.142", 8888))
# 5、关闭套接字
udp_socket.close()
