# 1.import psutil module
import psutil
import datetime

# 2.get cpu info
# 2.1 get cpu kernel num
print(psutil.cpu_count())
# get physical u kernel num
print(psutil.cpu_count(logical=False))
# 2.2 get cpu used percent
print(psutil.cpu_percent(interval=0.5))
print(psutil.cpu_percent(interval=0.5, percpu=True))

# 3.get memory info
# 3.1 get total memory info
print(psutil.virtual_memory())
# 3.2 get memory used percent
print(psutil.virtual_memory().percent)

# 4.get disk info
# 4.1 get disk partition info
print(psutil.disk_partitions())
# 4.2 get info for spec dir
print(psutil.disk_usage('/'))
# 4.3 get disk percent
print(psutil.disk_usage('/').percent)

# 5.get network info
# 5.1 get recevie pack number
print(psutil.net_io_counters().bytes_recv)
# 5.2 get send pack number
print(psutil.net_io_counters().bytes_sent)

# 6.get startup time
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
