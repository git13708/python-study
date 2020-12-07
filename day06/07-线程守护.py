import time
import threading


def work1():
    for i in range(10):
        print("正在执行work1:%d" % i)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建子线程
    # 1、导入模块
    # 2、创建线程对象
    # thread_work = threading.Thread(target=work1)
    thread_work = threading.Thread(target=work1, daemon=True)
    # 线程守护：子线程守护主线程
    # setDaemon(True)表示子线程就守护主线程（主线程结束后，子线程也结束）
    thread_work.setDaemon(True)
    # 3、启动子线程
    thread_work.start()
    time.sleep(2)
    print("Game Over!!")
    # 让程序退出，主线程主动结束
    exit(-1)
