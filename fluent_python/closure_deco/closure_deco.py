""" Closure and deco some concepts """
from functools import lru_cache


# Class approach
class Averager:
    def __init__(self):
        self.series = []  # closure

    def __call__(self, new_value):
        self.series.append(new_value)  # free variable
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
avg(10)


# Functional approach
def make_average():
    series = []  # closure

    def averager(new_value):
        series.append(new_value)  # free variable
        total = sum(series)
        return total / len(series)

    return averager


# series is freevar closure
avg = make_average()
avg(10)
avg(20)

vars_func = avg.__code__.co_varnames
free_var_closure = avg.__code__.co_freevars  # closure series[]
series_content = avg.__closure__[0].cell_contents  # all values in series closure


def make_averager_without_history_list():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total  # count = count + 1, assigning count = so it is not global so non local will solve this
        count += 1
        total += new_value
        return total / count

    return averager


# Functools cache for repeated call
# from functools import lru_cache

@lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print('6!= ', fibonacci(6))
