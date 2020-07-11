import time
import threading

def get_from_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html end')

def get_from_url(url):
    print('get detail url started')
    time.sleep(2)
    print('get detail url end')

th1 = threading.Thread(target=get_from_html, args=('', ))
th2 = threading.Thread(target=get_from_url, args=('', ))
th1.setDaemon(True)           # 如果为True则当主线程执行完时杀死子线程
th2.setDaemon(True)           # 默认为False，即主进程执行完会等待子线程也执行完
start_time = time.time()
th1.start()
th2.start()
# th1.join()        # 等待两个子线程执行完才继续执行主线程
# th2.join()        # 两个子线程是并发执行的，所以等待时间为2s，而不是4s
print(time.time() - start_time)
