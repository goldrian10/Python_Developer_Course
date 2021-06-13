# Main file
# import utility
from utility import *
import pyjokes
# A package is a folder that contains modules
# you should have a __init.py__ on the package as a rule
# import shopping.shopping_cart
# from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart
import random
import sys

print(__name__)
if __name__ == '__main__':
    (print('please run this'))
    print(divide(20, 5))
    print(multiply(2, 3))
    print(shopping_cart.buy('apple'))

# (random)
# print(dir(random))
# import random as alias

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
########################################

# $python3 code.py esteban naranjo
# file_name = sys.argv[0]
# first_name = sys.argv[1]
# second_name = sys.argv[2]

# help(pyjokes)

joke = pyjokes.get_joke('es', 'neutral')

print(joke)

# pipenv
# virtual environments you can install libraries and these does not affect other projects/ environments

# usefull modules
from collections import Counter, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 7]

print(Counter(li)) # create a counter object that keeps track how many time an item occurs on an iterable

sentence = 'blah blahaaaablhaaahahaa'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exists', {'a': 1, 'b': 2})
print(dictionary['cadsda'])

import datetime

print(datetime.time(5, 32, 2))
print(datetime.date.today())

from array import array

# lists in python are dynamic we can make it as big a we need
# arrays perform faster and take up less memory, it s not dynamic
arr = array('i', [1, 2, 3])
print(arr[0])




