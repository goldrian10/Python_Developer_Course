# generators only use one memory space, a list in example create store all the list in different
# memory spaces, the whole list will be taken space in memory

# generators are iterable
# all the generators are iterable but not all the iterables are generators

# def generator_func(num):
#     for i in range(num):
#         yield i  # yield pauses the functions momentarily
#
#
# for item in generator_func(1000):
#     print(item)
#
#
# def generator_func2(num):
#     for i in range(num):
#         yield i * 2  # yield pauses the functions momentarily
#
#
# g = generator_func2(5)
# print(g)
# next(g)
# next(g)
# print(next(g))
# print(next(g))


# Gen vs list

from time import time


def performance(fn):
    def wrap(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'this function did take {t2 - t1} s')
        return result

    return wrap


# @performance
# def long_time():
#     print('1')
#     for i in range(100000000):
#         i * 5
#
#
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(100000000)):
#         i * 5
#
#
# long_time()
# long_time2()


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])


class Mygen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if Mygen.current < self.last:
            num = Mygen.current
            Mygen.current += 1
            return num
        raise StopIteration


gen = Mygen(0, 100)


# for i in gen:
#     print(i)

@performance
def fib():
    keep1 = 0
    keep2 = 0
    for i in range(100000):
        if i == 0:
            pass
        if i == 1:
            keep1 = 1
            result = 1
        else:
            result = keep1 + keep2
            keep2 = keep1
            keep1 = result
        yield result

fib()


# fibo = fib(100)
# for i in range(20): print(f'fibonnaci of {i} is {next(fibo)}')

@performance
def fib2():
    a = 0
    b = 1
    i = 0
    for i in range(1000000):
        yield a
        temp = a
        a = b
        b = temp + b


fib2()



@performance
def fib3():
    a = 0
    b = 1
    i = 0
    result = []
    for i in range(1000000):
        result.append(a)
        temp = a
        a = b
        b = temp + b


fib3()
