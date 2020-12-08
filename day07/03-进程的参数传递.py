"""
1、导入模块
2、通过模块提供的Process类创建进程对象
3、启动进程
"""
import time
import multiprocessing


def work1(a, b, c):
    print("参数:", a, b, c)
    for i in range(10):
        print("正在运行 work1......")
        time.sleep(0.5)


if __name__ == '__main__':
    # 1、导入模块
    # 2、通过模块提供的Process类创建进程对象
    # 1) 使用args 传递元组
    # 2）使用kwagrs 传递字典
    # 3）混合使用 使用args  使用kwagrs
    # pro_obj = multiprocessing.Process(target=work1, args=(10, 100, 1000))
    # pro_obj = multiprocessing.Process(target=work1, kwargs={"a": 10, "b": 100, "c": 1000})
    pro_obj = multiprocessing.Process(target=work1,args=(10, ), kwargs={"b": 100, "c": 1000})
    # 3、启动进程
    pro_obj.start()
    print("xxxxxx")
