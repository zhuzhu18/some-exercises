import threading
import time

class GetFromHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print('get html started')
        time.sleep(2)
        print('get html end')

class GetFromUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)
    def run(self):
        print('get url started')
        time.sleep(2)
        print('get url end')

th1 = GetFromHtml(name='线程1')
th2 = GetFromUrl(name='线程2')
th1.start()
th2.start()
th1.join()
th2.join()
print('执行主线程')
