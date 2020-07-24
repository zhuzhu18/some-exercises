def gen_fib(index):
    a, b = 0, 1
    i = 0
    while i < index:
        a, b = b, a + b
        yield a
        i += 1

for k in gen_fib(10):     # 生成10个斐波那契数字, 该函数返回的是一个生成器对象, 实现了迭代协议
    print(k)
