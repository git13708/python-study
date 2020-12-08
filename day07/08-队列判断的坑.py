import multiprocessing

# 创建队列
queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(2)
queue.put(3)

# 判断队列是否为空
isEmpty = queue.empty()
print("isEmpty:", isEmpty)
