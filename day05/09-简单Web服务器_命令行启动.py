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
import sys
from application import app

# ws = WebServer()
# ws.start()


class WebServer(object):
    # 初始化方法
    def __init__(self, port):
        # 1、导入模块
        # 2、创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 3、设置地址重用
        # socket.SOL_SOCKET 当前套接字
        # socket.SO_REUSEADDR 地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 4、绑定端口
        tcp_server_socket.bind(("", port))
        # 5、设置监听，让套接字由主动变为被动接收
        tcp_server_socket.listen(128)
        # 定义示例属性，保存套接字对象
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        """启动web服务器"""
        print("Web服务器已经启动...等待客户端连接中......")
        # 6、接受客户端连接 定义函数 request_handler()
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户端[%s]上线了" % str(ip_port))
            # 调用功能函数
            self.request_handler(new_client_socket, ip_port)

    def request_handler(self, new_client_socket, ip_port):
        """接收信息，并且做出响应"""
        # 7、接收客户端浏览器发送的请求协议
        request_data = new_client_socket.recv(1024)
        # print(request_data)
        # 8、判断协议是否为空
        if not request_data:
            print("客户端[%s]已经下线了" % str(ip_port))
            new_client_socket.close()
            return
        # 使用 application 文件夹 app模块
        response_data = app.application("static", request_data, ip_port)
        # 10、发送响应报文
        new_client_socket.send(response_data)
        # 11、关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""
    """
    1、导入sys模块
    2、获取系统传递到程序的参数
    3、判断参数格式是否正确
    4、判断端口号是否是一个数字
    5、获取端口号
    6、再启动Web服务器的时候，使用获取的端口号
    """
    # 2、获取系统传递到程序的参数
    params_list = sys.argv
    # print(params_list)
    # 3、判断参数格式是否正确
    if len(params_list) != 2:
        print("启动失败，参数格式错误！正确格式：python3 xxx.py 端口号")
        return
    # 4、判断端口号是否是一个数字
    if not params_list[1].isdigit():
        print("启动失败，端口号不是一个纯数字！")
        return
    # 5、获取端口号
    port = int(params_list[1])
    # 6、再启动Web服务器的时候，使用获取的端口号

    # 创建WebServer类的对象
    ws = WebServer(port)
    # 对象.start() 启动web服务器
    ws.start()
    # 11、关闭连接
    # tcp_server_socket.close()


if __name__ == '__main__':
    main()
