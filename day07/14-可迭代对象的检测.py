"""
isinstaance(待检测的对象， Iterable)
返回值：True 可以迭代
       Flase 不可以迭代
"""
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))


# 自定义一个类
class MyClass(object):
    # 增加一个__iter__方法
    # 该方法就是一个迭代器
    def __iter__(self):
        pass


# 创建对象
myclass = MyClass()
print(isinstance(myclass, Iterable))

# 1、可遍历对象就是可迭代对象
# 2、列表、元组、字典、字符串都是可迭代对象
# 3、100 和自定义myclass默认都是不可以迭代的
# 4、myclass对象所属的类MyClass 如果包含了__iter__()方法，此是myclass就是一个可迭代对象
# 5、可迭代对象的本质：对象所属的类中包含了 __iter__()方法
# 6、检测一个对象是否可以迭代，用isinstance（）函数检测
