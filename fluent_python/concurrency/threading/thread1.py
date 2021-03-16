# Example 1
import threading
import time

start = time.perf_counter()


def do_something(second=1):
    print(f'Sleeping {second} sec')
    time.sleep(second)
    print('Done sleeping')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()  # Waits until two threads finish go to next line

finish = time.perf_counter()

print(f'Example 1: Finished in {round(finish - start, 2)} seconds')

# -----------------------------------------------------------------
# Example 2 - run 1- seconds func to 1 second

start = time.perf_counter()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])  # args to do something func
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Exaple 2 : Finished in {round(finish - start, 2)} seconds')


