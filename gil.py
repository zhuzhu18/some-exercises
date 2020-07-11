import dis
import threading

# gil = global interpreter lock(cpython)
# python中一个线程对应于C语言中的一个线程
# gil使同一时刻只有一个线程在一个CPU上执行字节码，无法将多个线程映射到多个CPU上执行

# gil会根据执行的字节码行数或时间片释放gil，gil在遇到io操作时也会主动释放
total = 0
def add():
    global total
    for i in range(1000000):
        total += 1

def desc():
    global total
    for i in range(1000000):
        total -= 1

# print(dis.dis(add))        # 查看add函数的字节码
th1 = threading.Thread(target=add)
th2 = threading.Thread(target=desc)
th1.start()
th2.start()
print(total)
