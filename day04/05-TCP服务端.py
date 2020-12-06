"""
1、导入模块
2、创建套接字
3、绑定端口
4、开启监听（设置套接字为被动模式）
5、等待客户端连接
6、收发数据
7、关闭连接
"""
# 1、导入模块
import socket
# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、绑定端口
tcp_server_socket.bind(("", 8888))
# 4、开启监听（设置套接字为被动模式）
# listen() 作用设置tcp_server_socket套接字为被动监听模式，不能再主动发送数据
# 128 允许接受的最大的连接数，再windows 128有效，但是再linux 此数字无效
tcp_server_socket.listen(128)
# 5、等待客户端连接
# accept开始接受客户端连接,程序会默认进入阻塞状态（等待客户端连接），如果有客户端连接后，程序自动向下执行
# 1)返回了一个新的套接字socket
# 2)客户端的ip地址和端口号 元组
new_client_socket, ip_port = tcp_server_socket.accept()
# print(new_client_socket, ip_port)
print("新客户端上线了：%s" % str(ip_port))
# 6、收发数据
# recv()会让程序再次阻塞，收到信息后继续向后执行
recv_data = new_client_socket.recv(1024)
recv_text = recv_data.decode("GBK")
print(recv_text)
# new_client_socket.close() 表示不能再和当前的客户端通信了
new_client_socket.close()
# 7、关闭连接
# tcp_server_socket.close() 表示程序不再接受新的客户端，已经连接的可以继续服务
tcp_server_socket.close()
print("关闭服务器中......")
print("连接已关闭")
