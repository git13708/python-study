"""
思路：
1、准备两个进程
2、准备一个队列 一个进程向队列中写入数据，然后把队列传递到另外一个进程
3、另外一个进程读取数据

"""
import time
import multiprocessing


# 写入数据到队里的函数
def write_queue(cqueue):
    # for 循环，向队列写入数据
    for i in range(10):
        # 判断队列是否已满
        if cqueue.full():
            print("队列已满")
            break
        # 向队列中放入值
        cqueue.put(i)
        print("写入成功，已经写入：", i)
        time.sleep(0.5)


# 读取队列数据并显示的函数
def read_queue(cqueue):
    while True:
        # 判断队列是否为空
        if cqueue.qsize() == 0:
            print("队列已空")
            break
        # 从队列中读取数据
        value = cqueue.get()
        print("已经读取：", value)


if __name__ == '__main__':
    # 1、创建进程池
    pool = multiprocessing.Pool(2)
    # 2、创建进程池中的队列
    queue = multiprocessing.Manager().Queue(5)
    # 3、使用进程池执行任务

    # pool.apply(write_queue, args=(queue, ))
    # pool.apply(read_queue, args=(queue,))
    # 4、异步方式执行
    # apply_async()返回值 ApplyResult对象，该对象由一个wait()的方法
    # wait()方法类似Join 表示先让当前进程执行完毕 后续进程才能启动
    result = pool.apply_async(write_queue, args=(queue, ))
    result.wait()
    pool.apply_async(read_queue, args=(queue,))
    # close表示不再接收新的任务
    pool.close()
    # join表示主线程等待线程池执行结束后再退出
    pool.join()
