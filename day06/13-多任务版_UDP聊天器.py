"""
一、功能
1、发送信息
2、接收消息
3、退出系统

二、框架的设计
1、发送信息 send_msg()
2、接收信息 recv_msg()
3、程序的主入口 main()
4、当程序独立运行的时候，才启动聊天器

三、实现步骤
1、发送消息 send_msg()
1)定义变量接收用户与输入的接收方的IP地址
2)定义变量接收用户与输入的接收方的端口号
3)定义变量接收用户与输入的接收方的内容
4）使用socket的sendto发送消息
2、接收消息 recv_msg()
1）使用socket 接收数据
2）解码数据
3）输出显示

3、主入口main()
1）创建套接字
2）绑定端口
3）打印菜单（循环）
4）接收用户输入的选项
5）判断用户的选择，并且调用对应的函数
6）关闭套接字

TCP传输特点
1、应答机制
2、超时重传
3、错误校验
4、流量控制和阻塞管理

TCP与UDP的不同点
1、面向连接（确认有创建三方交握，连接已创建才做传输）
2、有序数据传输
3、重发丢失的数据包
4、舍弃重复的数据包
5、无差错的数据传输
6、阻塞/流量控制
"""
import socket
import threading


def send_msg(udp_socket):
    """发送信息的函数"""
    # 1)定义变量接收用户与输入的接收方的IP地址
    ipaddr = input("请输入接收方的IP地址：\n")
    if len(ipaddr) == 0:
        ipaddr = "192.168.0.117"
        print("当前接收方IP地址默认设置为【%s】" % ipaddr)
    # 2)定义变量接收用户与输入的接收方的端口号
    port = input("请输入接收方的端口号：\n")
    if len(port) == 0:
        port = "8888"
        print("当前接收方端口默认设置为【%s】" % port)
    # 3)定义变量接收用户与输入的接收方的内容
    content = input("请输入接收方的内容：\n")
    if len(content) == 0:
        content = "测试系统信息"
        print("当前接收方内容默认设置为【%s】" % content)
    # 4）使用socket的sendto发送消息
    ret = udp_socket.sendto(content.encode(), (ipaddr, int(port)))
    print("发送结果：", ret)


def recv_msg(udp_socket):
    """接收信息的函数"""
    while True:
        # 1）使用socket接收数据
        recv_data, ip_port = udp_socket.recvfrom(1024)
        # 2）解码数据
        recv_text = recv_data.decode(encoding="UTF-8", errors="ignore")
        # 3）输出显示
        print("接收到来自[%s]的消息：%s" % (str(ip_port), recv_text))


def main():
    """程序的主入口"""
    # 1）创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2）绑定端口
    # address -> (“ip地址”， 端口号)
    udp_socket.bind(("", 8888))
    # 3) 创建子线程，单独接收用户的消息
    thread_recvmsg = threading.Thread(target=recv_msg, args=(udp_socket, ))
    thread_recvmsg.setDaemon(True)
    # 启动子线程
    thread_recvmsg.start()
    while True:
        # 3）打印菜单（循环）
        print("\n\n**************************************")
        print("***********    1、发送信息   ***********")
        print("***********    2、退出系统   ***********")
        print("**************************************")
        # 4）接收用户输入的选项
        sel_num = int(input("请输入选项：\n"))
        # 5）判断用户的选择，并且调用对应的函数
        if sel_num == 1:
            # print("您选择的是发送信息")
            # 调用发送信息的函数
            send_msg(udp_socket)
        elif sel_num == 2:
            print("系统正在退出中......")
            print("系统退出完成")
            break
    # 6）关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    # 程序独立运行的时候，才去启动聊天器
    main()