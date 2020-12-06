"""
1、导入模块
2、创建套接字
3、绑定端口
4、接收对方发送的数据
5、解码数据
6、输出显示
7、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、绑定端口
# ip地址尽可能写为“”，好处当计算机有多个网卡的时候，不同网卡的数据都能接收到
# udp_socket.bind(("192.168.0.117", 8888))
# udp_socket.bind(("", 8888))
# 4、接收对方发送的数据
recv_data, ip_port = udp_socket.recvfrom(1024)
# 5、解码数据
recv_text = recv_data.decode(encoding="GBK", errors="ignore")
# 6、输出显示
# print("来自：", ip_port[0], "的消息,", recv_text)
print("接收[%s]的信息：%s" % (str(ip_port[0]), recv_text))
# 7、关闭套接字
udp_socket.close()
