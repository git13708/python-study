"""
1、导入模块
2、通过模块提供的Process类创建进程对象
3、启动进程
"""
import time
import multiprocessing


def work1():
    for i in range(10):
        print("正在运行 work1......")
        time.sleep(0.5)


if __name__ == '__main__':
    # 1、导入模块
    # 2、通过模块提供的Process类创建进程对象
    pro_obj = multiprocessing.Process(target=work1)
    # 设置进程守护
    # pro_obj.daemon = True
    # 3、启动进程
    pro_obj.start()

    time.sleep(2)
    print("终止运行")
    # 终止子进程的执行
    pro_obj.terminate()
    exit(0)
