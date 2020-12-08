import multiprocessing
import time
# 定义全局变量
g_num = 10


# work1 对全局变量累加
def work1():
    global g_num
    for i in range(10):
        g_num += 1
    print("--------------------work1-------------------", g_num)


# work2 读取全局变量的值：如果能读取到，则全局变量能共享，否则不能共享的
def work2():
    print("--------------------work2-------------------", g_num)


# 定义两个进程
if __name__ == '__main__':
    # 创建进程
    pro_obj1 = multiprocessing.Process(target=work1)
    pro_obj2 = multiprocessing.Process(target=work2)
    # 启动进程
    pro_obj1.start()
    pro_obj2.start()

    time.sleep(3)
    print("--------------------main-------------------", g_num)
