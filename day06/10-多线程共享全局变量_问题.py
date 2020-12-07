import threading
import time
# 看看work1线程对全局变量的修改，再work2中能否查看修改后的结果
# 定义全局变量
g_num = 0


# work1
def work1():
    # 声明g_num是一个全局变量
    global g_num

    for i in range(1000000):
        g_num += 1
        # time.sleep(0.1)

    print("work1------", g_num)


# work2
def work2():
    # 声明g_num是一个全局变量
    global g_num

    for i in range(1000000):
        g_num += 1
        # time.sleep(0.1)
    print("work2------", g_num)  # g_num可以再多个线程中共享


if __name__ == '__main__':
    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    # 优先让t1线程优先执行，t1执行完毕后，t2才能执行
    t1.join()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)
    # 再t1和t2线程执行完毕后再打印g_num
    print("main ------", g_num)

