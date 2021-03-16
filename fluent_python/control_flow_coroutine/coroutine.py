""" Generator as a coroutine """
from inspect import getgeneratorstate
from functools import wraps
from collections import namedtuple


# ---------------------------------------------------------------------- #
def simple_coroutine(a):
    print('-> Started: a=', a)
    b = yield a
    print('-> Recieved: b=', b)
    c = yield b + a
    print('-> Recieved: c=', c)


cor_1 = simple_coroutine(12)
getgeneratorstate(cor_1)  # STARTED
next(cor_1)  # 12
getgeneratorstate(cor_1)  # SUSPENDED
cor_1.send(10)  # Recieved: b=10
cor_1.send(20)  # Recieved: c=20


# ---------------------------------------------------------------------- #
# Averager as coroutine
def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        value = yield average
        total += value
        count += 1
        average = total / count


coro_average = averager()
next(coro_average)  # init until yield None
coro_average.send(10)
coro_average.send(16)
average_value = coro_average.send(14)
float.is_integer(average_value)


# ---------------------------------------------------------------------- #
# Priming generator so that no next() is required before .send
def coroutine(func):
    """ Decorator: primes `func` by advancing to first `yield`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(args, kwargs)
        next(gen)
        return gen
    return primer


coroutine_gen = coroutine(averager)()  # Ready .send() rightaway
# or @coroutine as decorator


# ---------------------------------------------------------------------- #
# Catching StopIteration lets us get the value returned by averager
Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None

    while True:
        value = yield
        if value is None:
            break
        total += value
        count += 1
        average = total / count
    return Result(count, average)


coro_averager = averager()
next(coro_average)
coro_average.send(10)
coro_average.send(20)

try:
    coro_average.send(None)
except StopIteration as exc:
    result = exc.value  # result is Result


# ---------------------------------------------------------------------- #
# Yield From
def gen():
    for c in 'AB':
        yield c

    for i in range(1, 3):
        yield i


def gen_from():
    yield from 'AB'
    yield from range(1, 2)
# list(gen()) == list(gen_from())


def chain(*iterables):
    for it in iterables:
        yield from it


list_of_value = list(chain('ABC', range(1, 3), 'DEF'))
# ---------------------------------------------------------------------- #

