import multiprocessing

# Here we create separate processes, with different heaps
# You can also create threads, that share the same heap.
# See 'multithreading.py'
# More examples here: https://pymotw.com/3/multiprocessing/basics.html

def worker():
    """worker function"""   
    print('Worker')


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()