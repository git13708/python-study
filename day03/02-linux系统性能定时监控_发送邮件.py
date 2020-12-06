import psutil
import datetime
import yagmail


def linux_monitor(time):
    """define function ,implement get physic info"""
    cpu_per = psutil.cpu_percent(interval=time)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    net_info = psutil.net_io_counters()
    current_time = datetime.datetime.now().strftime("%F %T")

    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
    psutil.cpu_count(logical=False), memory_info.total / 1024 / 1024 / 1024, disk_info.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s   |\n" % (
    current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
    log_str += "|-------------------|------------------------|-------------|----------------------------|\n"

    print(log_str)

    # 写入文件
    with open("log.txt", 'a') as f:
        f.write(log_str + "\n\n")
    # 判断条件 内存使用率超过80% CPU超过80%
    if cpu_per > 80 or memory_info.percent > 80:
        # 发送邮件
        ya_obj = yagmail.SMTP(user="wy13708@163.com", password="CMZVHFZVRQWATMUS", host="smtp.163.com")
        ya_obj.send(to="2482432123@qq.com", subject="系统监控信息", contents=log_str)
        print("发送邮件成功")


def main():
    """program entrance"""
    while True:
        linux_monitor(10)


if __name__ == '__main__':
    main()
