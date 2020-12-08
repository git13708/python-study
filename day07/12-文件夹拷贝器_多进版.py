"""
1、定义变量，保存文件夹，目标文件夹所在的路径
2、在目标路径创建新的文件夹
3、获取源文件夹中的所有文件（列表）
4、遍历列表，得到所有的文件名
5、定义函数，进行文件拷贝

文件拷贝函数：
参数：源文件路径 目标文件夹路径 文件名
1、拼接源文件和目录文件的具体路径
2、打开源文件，创建目标文件
3、读取源文件的内容，写到目标文件中
"""
import os
import multiprocessing


def copy_work(source_dir, dest_dir, file_name):
    """根据参数，拷贝文件"""
    print(multiprocessing.current_process())
    # 1、拼接源文件和目录文件的具体路径
    # ./test/1.txt ----> /home/wangqiang/桌面/test/1.txt

    # 2、打开源文件，创建目标文件
    source_path = source_dir+"/"+file_name
    dest_path = dest_dir+"/"+file_name
    # print(source_path, dest_path)
    # 3、读取源文件的内容，写到目标文件中
    with open(source_path, "rb") as source_file:
        # 创建目标文件
        with open(dest_path, "wb") as dest_file:
            while True:
                # 读源文件保存到目标文件
                file_data = source_file.read(1024)
                if file_data:
                    dest_file.write(file_data)
                else:
                    break


if __name__ == '__main__':
    # 1、定义变量，保存文件夹，目标文件夹所在的路径
    source_dir = "./test"
    dest_dir = "/home/wangqiang/桌面/test"

    # 2、在目标路径创建新的文件夹
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    else:
        print("目标文件夹已存在")
    # 3、获取源文件夹中的所有文件（列表）
    file_list = os.listdir(source_dir)

    # 创建进程池
    pool = multiprocessing.Pool(3)
    # 4、遍历列表，得到所有的文件名
    for file_name in file_list:
        # print(file_name)
        # 5、定义函数，进行文件拷贝
        # copy_work(source_dir, dest_dir, file_name)
        pool.apply_async(copy_work, (source_dir, dest_dir, file_name))
    pool.close()
    pool.join()

