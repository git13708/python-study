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
# recvfrom方法的作用
# 1）从套接字中接收2048个字节的数据
# 2）此方法会造成程序的阻塞，等待另外一台计算机发来的数据
#    如果对方发送数据了，就会解除阻塞
#    如果对方没有发送数据，会一直等待
# recv_data = (b'36363', ('192.168.0.142', 8888))
# 接收到的数据是一个元组：1）接收到的二进制数据 2）发送方的ip地址和端口号
recv_data = udp_socket.recvfrom(2048)
print(recv_data)
# 5、解码数据，得到字符串
recv_text = recv_data[0].decode("GBK")
# 6、输出显示接收到的内容
print("来自：", recv_data[1][0], "的消息,", recv_text)
# 7、关闭套接字
udp_socket.close()
