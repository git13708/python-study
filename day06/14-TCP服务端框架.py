"""
1、导入模块
2、创建套接字
3、设置地址可以重用
4、绑定端口
5、设置监听，套接字由主动变为被动
6、接收客户端连接
7、接收客户端发送的信息
8、解码数据并且输出
9、关闭当前客户端的连接
"""
# 1、导入模块
import socket
import threading


def recv_msg(new_client_socket, ip_port):
    while True:
        # 7、接收客户端发送的信息
        recv_data = new_client_socket.recv(1024)
        if recv_data:
            # 8、解码数据并且输出
            recv_text = recv_data.decode("GBK")
            print("收到来自【%s】的信息：%s" % (str(ip_port), recv_text))
        else:
            break
    # 9、关闭当前客户端的连接
    new_client_socket.close()


# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、设置地址可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 4、绑定端口
tcp_server_socket.bind(("", 8080))
# 5、设置监听，套接字由主动变为被动
tcp_server_socket.listen(128)
while True:
    # 6、接收客户端连接
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("新客户端【%s】上线了" % str(ip_port))
    # recv_msg(new_client_socket, ip_port)
    # 创建线程
    thread_recvmsg = threading.Thread(target=recv_msg, args=(new_client_socket, ip_port))
    # 设置守护线程
    thread_recvmsg.setDaemon(True)
    # 启动线程
    thread_recvmsg.start()

# tcp_server_socket.close()
