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
import multiprocessing
from application import app

# ws = WebServer()
# ws.start()

"""
1、在类的初始化方法中配置当前的项目
{"2048":"./2048", "植物大战僵尸v1":"./zwdzjs-v1"}
2、给类增加一个初始化项目配置方法 init_projects()
2.1 显示所有可以发布的游戏 菜单
2.2 接收用户的选择
2.3 根据用户的选择发布指定的项目（保存用户选择的游戏对应的本地目录）
3、更改web服务器打开的文件目录
"""


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

        # 定义类的实例属性 projects_dict 初始化为空
        self.projects_dict = dict()
        # 定义实例属性，保存要发布的游戏
        self.current_dir = ""
        #                      key                    value
        self.projects_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物大战僵尸-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝卜'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读心术'] = "dxs"

        # print(self.projects_dict)

        # 调用初始化游戏项目的方法
        self.init_projects()

    # 添加一个初始化项目的方法
    def init_projects(self):
        # 2.1显示所有可以发布的游戏菜单
        # list(self.projects_dict.keys()) 取出字典的key 并且转换为列表
        keys_list = list(self.projects_dict.keys())
        # 遍历显示所有的key
        # [(0,"xxx"),(1,"yyy"),(2,"zzz")]
        for index, game_name in enumerate(keys_list):
            # print(str(index)+"、"+game_name)
            print("%d.%s" % (index, game_name))
        # 2.2接收用户的选择
        sel_no = int(input("请选择要发布的游戏序号：\n"))
        # 2.3根据用户的选择发布指定的项目（保存用户选择的游戏对应的本地目录）
        # 根据用户的选择，得到游戏的名称（字典的key）
        key = keys_list[sel_no]
        # 根据字典的key 得到项目的具体路径
        self.current_dir = self.projects_dict[key]
        # print(key, current_dir)

    def start(self):
        """启动web服务器"""
        print("Web服务器已经启动...等待客户端连接中......")
        # 6、接受客户端连接 定义函数 request_handler()
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户端[%s]上线了" % str(ip_port))
            # 调用功能函数
            # self.request_handler(new_client_socket, ip_port)
            # 进程使用分3步
            # 1）导入模块
            # 2）创建进程对象
            p1 = multiprocessing.Process(target=self.request_handler, args=(new_client_socket, ip_port))
            # 3）启动进程
            p1.start()
            # 子进程运行会拷贝主进程的资源
            new_client_socket.close()


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
        response_data = app.application(self.current_dir, request_data, ip_port)
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
