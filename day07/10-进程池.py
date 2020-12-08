"""
1、创建一个函数 用于模拟文件拷贝
2、创建一个进程池 长度3 表示进程池中最多创建3文化进程
3、先用进程池同步方式拷贝文件
4、再用异步工作方式拷贝文件
"""
import time
import multiprocessing


# 1、创建一个函数 用于模拟文件拷贝
def copy_work():
    print("正在拷贝文件......", multiprocessing.current_process())
    time.sleep(0.5)


if __name__ == '__main__':
    # 2、创建一个进程池 长度3 表示进程池中最多创建3文化进程
    # 进程池创建，有两步：
    # 1）导入模块
    # 2）创建进程池 multiprocessing.Pool(2) 最大允许创建2个进程
    pool = multiprocessing.Pool(3)
    # for i in range(10):
    #     copy_work()
    for i in range(10):
        # pool.apply(函数名, 传递给函数的参数)
        # 3、先用进程池同步方式拷贝文件
        # pool.apply(copy_work)

        # 4、再用异步工作方式拷贝文件
        # 如果使用apply_async方式，需要做两点：
        # 1）pool.close()表示不再接收新的任务
        # 2）主进程不再等待线程池执行结束后再退出，需要进程池join()
        # pool.join()让主进程池等待进程池执行接收后再退出
        pool.apply_async(copy_work)

    # pool.close()表示不再接收新的任务,pool是可用的
    pool.close()
    # pool.join()让主进程池等待进程池执行接收后再退出
    pool.join()
