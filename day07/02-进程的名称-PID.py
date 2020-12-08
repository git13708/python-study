"""
1、导入模块
2、通过模块提供的Process类创建进程对象
3、启动进程
"""
import time
import multiprocessing
import os


def work1():
    for i in range(50):
        # print("正在运行 work1......", multiprocessing.current_process())
        # 获取进程的编号
        # print("正在运行 work1......", multiprocessing.current_process().pid)
        # print("正在运行 work1......", os.getpid())
        # 获取进程的父id ppid -> parent process id
        print("正在运行 work1......", i, os.getpid(), "->父ID", os.getppid())
        time.sleep(2)


if __name__ == '__main__':
    # 获取主进程名称
    print(multiprocessing.current_process())
    # 获取的进程的编号
    # 1) multiprocessing.current_process().pid 进程编号
    print(multiprocessing.current_process().pid)
    # 2）使用os模块来获取
    print("主进程编号:", os.getpid())
    # 1、导入模块
    # 2、通过模块提供的Process类创建进程对象
    # target 指定子进程执行的分支函数
    # name 指定子进程的名称
    pro_obj = multiprocessing.Process(target=work1, name="p1")
    # 3、启动进程
    pro_obj.start()
    print("xxxxxx")
