# Example 1
import multiprocessing
import time


start = time.perf_counter()

def do_something(second=1):
    print(f'Sleeping {second} sec')
    time.sleep(second)
    print('Done sleeping')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join() # Waits until two threads finish go to next line

finish = time.perf_counter()

print(f'Example 1: Finished in {round(finish - start, 2)} seconds')


# -----------------------------------------------------------------
# Example 2 - run 1- seconds func to 1 second

start = time.perf_counter()

processes = []

for _ in range(10):
    t = multiprocessing.Process(target=do_something, args=[1.5]) # args to do something func, args to must be packleable
    t.start()
    processes.append(t)

for processe in processes:
    processe.join()

finish = time.perf_counter()

print(f'Exaple 2 : Finished in {round(finish - start, 2)} seconds')