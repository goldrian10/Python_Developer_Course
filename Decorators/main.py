# Decorators

def my_decorator(func):
    def wrap_func():
        print('******************')
        func()
        print('******************')

    return wrap_func


@my_decorator
def hello():
    print('Hellooooo')


@my_decorator
def bye():
    print('byeeeee')


hello()
bye()


def my_decorator(func):  # decorator template
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)

    return wrap_func


@my_decorator
def hello(greeetings):
    print(greeetings)


@my_decorator
def bye():
    print('byeeeee')


hello('hiiii')
bye()

# Decorator
from time import time


def performance(fn):
    def wrap(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'it took {t2 - t1} s')
        return result

    return wrap


@performance
def long_time(t):
    x = 0
    for i in range(t):
        x += 1
    return x


print(long_time(10000000))

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrap(*args, **kwargs):
        if user1['valid']:  # if args[0]['valid']
            fn(*args, **kwargs)
            return fn
        # return None

    return wrap


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
