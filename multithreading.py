import threading
import time

# Here we create separate threads, that share the same heap.
# You can also create processes, with different heaps.
# See 'multiprocessing-example.py'
# Further info: https://pymotw.com/3/threading/index.html

def worker():
    """thread worker function"""
    print('Starting Worker for thread %s' % threading.current_thread().getName())
    time.sleep(1.5)
    print('Ending thread %s' % threading.current_thread().getName())

def workerWithArgs(str):    
    print('WorkerWithArgs received: %s' % str)
    


threads = []
for i in range(5):
    t = threading.Thread(target=worker, name='thread-'+ str(i))
    threads.append(t)
    t.start()

    threading.Thread(target=workerWithArgs, args=('hello',)).start()