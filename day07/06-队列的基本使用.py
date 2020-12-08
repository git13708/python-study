"""
队列就multiprocessing 模块提供的一个类
1）创建队列（需要指定长度）
2）放值
3）取值
"""
import multiprocessing
# 1）创建队列（需要指定长度）
# multiprocessing.Queue(n) n表示队列长度
queue = multiprocessing.Queue(5)
# 2）放值
# queue.put()向队列中放值
queue.put(1)  # 放入1数字
queue.put("hello")
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({"a": 10, "b": 100})
# 长度为5 放入第6个数据后，队列就进入阻塞状态，默认会等待队列先取出来再放入新的值
# queue.put(10)
# queue.put_nowait(10)  # 表示放入值，如果已满，不再等待，直接报错
# 3）取值
print(queue.get())
print("--"*20)

print(queue.get())
print("--"*20)

print(queue.get())
print("--"*20)

print(queue.get())
print("--"*20)

print(queue.get())
print("--"*20)
# -----------------------队列中已经没有值了--------------
# 当队列已经空的时候，再此get() 程序进入阻塞状态，等待放入新的值到队列，然后再取
# print(queue.get())
# print("--"*20)
# get_nowait() 当队列已空的时候，不会等待放入新的值，直接报错
print(queue.get_nowait())
print("--"*20)
