"""
1、导入模块
2、创建套接字
3、发送数据
4、接收数据（二进制）
5、解码数据，得到字符串
6、输出显示接收到的内容
7、关闭套接字
"""
# 1、导入模块
import socket
# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、发送数据
udp_socket.sendto("约吗？".encode("GBK"), ("192.168.0.142", 8888))
# 4、接收数据（二进制）
recv_data = udp_socket.recvfrom(2048)
print(recv_data)
# 5、解码数据，得到字符串
# encoding指定解码格式
# errors出现错误后，如何处理 strict：严格模式 ignore：忽略模式
# decode(encoding="UTF-8",errors="")
recv_text = recv_data[0].decode(encoding="UTF-8", errors="ignore")
# 6、输出显示接收到的内容
print("来自：", recv_data[1][0], "的消息,", recv_text)
# 7、关闭套接字
udp_socket.close()
