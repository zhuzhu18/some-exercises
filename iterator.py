from collections.abc import Iterable, Iterator

class Company:
    def __init__(self, a):
        self.emplloyees = a
        self.index = 0

    def __iter__(self):       # Company实现了__iter__方法，所以com是一个Iterable对象, 并且__iter__方法必须返回一个迭代器
        return self

    def __next__(self):       # 同时实现了__next__方法，所以com也是一个Iterator对象
        try:
            v = self.emplloyees[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return v

com = Company(['zhu', 'zhi', 'hua'])
# for a in com:       # 也可以采用for循环来遍历, for循环能自动处理StopIteration异常
#     print(a)
while True:
    try:
        print(next(com))
    except StopIteration:
        break
