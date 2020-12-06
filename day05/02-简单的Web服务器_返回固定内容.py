"""
TCP 服务器
1、导入模块
2、创建套接字
3、设置地址重用
4、绑定端口
5、设置监听，让套接字由主动变为被动接收
6、接受客户端连接 定义函数 request_handler()
7、接收客户端浏览器发送的请求协议
8、判断协议是否为空
9、拼接响应的报文
10、发送响应报文
11、关闭连接
"""
import socket


def request_handler(new_client_socket, ip_port):
    """接收信息，并且做出响应"""
    # 7、接收客户端浏览器发送的请求协议
    request_data = new_client_socket.recv(1024)
    # print(request_data)
    # 8、判断协议是否为空
    if not request_data:
        print("客户端[%s]已经下线了" % str(ip_port))
        new_client_socket.close()
        return
    # 9、拼接响应的报文
    # 9.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 9.2 响应头
    response_header = "Server: Python20WS/1.1\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应主体
    response_body = "<h1>hello world</h1>"
    response_data = response_line + response_header + response_blank + response_body
    # 10、发送响应报文
    new_client_socket.send(response_data.encode())
    # 11、关闭当前连接
    new_client_socket.close()

def main():
    """主函数"""
    # 1、导入模块
    # 2、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3、设置地址重用
    # socket.SOL_SOCKET 当前套接字
    # socket.SO_REUSEADDR 地址重用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 4、绑定端口
    tcp_server_socket.bind(("", 8080))
    # 5、设置监听，让套接字由主动变为被动接收
    tcp_server_socket.listen(128)
    # 6、接受客户端连接 定义函数 request_handler()
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("新客户端[%s]上线了" % str(ip_port))
        # 调用功能函数
        request_handler(new_client_socket, ip_port)
    # 11、关闭连接
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
