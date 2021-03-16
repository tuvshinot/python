# Example 3
import concurrent.futures
import time

start = time.perf_counter()

def do_something(second=1):
    print(f'Sleeping {second} sec')
    time.sleep(second)
    return f'Done sleeping {second}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1.3) # second=1.3
    f2 = executor.submit(do_something, 1.3) # second=1.3
    print(f1.result())
    print(f2.result())


finish = time.perf_counter()

print(f'Exaple 3 : Finished in {round(finish - start, 2)} seconds')
print('-----------------------------------------------------------')

# ----------------------------------------------------------------
# Example 4 running 10 times, first to finish comes out first

start = time.perf_counter()


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(do_something, i) for i in range(5, 1, -1)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Exaple 4 : Finished in {round(finish - start, 2)} seconds')
print('-----------------------------------------------------------')

# ----------------------------------------------------------------
# Example 5, finishes order that they started, first finishes 5. because 5 was called first

start = time.perf_counter()


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(do_something, range(5, 1, -1))
    
    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Exaple 5 : Finished in {round(finish - start, 2)} seconds')
print('-----------------------------------------------------------')
