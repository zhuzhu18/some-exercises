import numpy as np
'''
函数调用和赋值,都是在引用,既不拷贝对象也不拷贝数据
'''
def fun(x):
    # 形参也是对实参的引用,改变形参的值会改变实参的值
    print(id(x))
    return x

a = np.arange(6)
c = a
print(id(a))
b = fun(a)
print(b is a)      # True
print(c is a)      # True


'''
浅拷贝,拷贝对象但不拷贝数据
不同的数组对象可以共用相同的数据,但它们的id不同
'''
# b = a.view()
# print(b is a)      # False
# b.shape = 2,3
# b[1, 0] = 100
# print(b)         # b:[[0, 1, 2], [100, 4, 5]]
# print(a)         # [0, 1, 2, 100, 4, 5]


'''
切片相当于引用,共用数据但分别属于不同的对象
'''
# x = a[:4]
# print(x.base is a)         # True
# print(x.flags.owndata)     # False
# print(x)
# del a       # 由于x引用了a,所以即使执行del a,a仍然存在于内存中
# print(x.flags.owndata)     # False
# print(x.base)              # [0, 1, 2, 3, 4, 5]



'''
深拷贝,既拷贝对象也拷贝数据
'''
# m = a.copy()
# print(m is a)       # False
# m[0] = 100
# print(a)        # [0 1 2 3 4 5]
