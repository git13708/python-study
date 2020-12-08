"""
1、判断是否已满
2、判断是否已经为空
3、取出队列中消息的个数
"""
import multiprocessing
import multiprocessing
# 创建一个长度为3的队列
queue = multiprocessing.Queue(3)
# 放值
queue.put(1)
queue.put(2)
queue.put(3)

# 取值
value = queue.get()

# 1、判断是否已满
isFull = queue.full()
print("isFull:", isFull)
# 2、判断是否已经为空
isEmpty = queue.empty()
print("isEmpty:", isEmpty)
value = queue.get()
# 3、取出队列中消息的个数
print("消息的个数：", queue.qsize())

