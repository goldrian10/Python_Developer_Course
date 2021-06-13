# Functional programming
# Pure function has two rules
# 1 For the same input it should result to the same output
# 2 Should not produce any side effects

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([1, 2, 3]))

# map, filter, zip, reduce
# map: usable every time that you need to iterate over something

my_list = [1, 2, 3]


def multiply_by2_map(item):
    return item * 2


print(list(map(multiply_by2_map, my_list)))
print(my_list)


# filter: add to the list the values true

def only_odd(item):
    return item % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)

# zip: we need two list or two iterable and zipped it together
your_list = [10, 20, 30]
their_list = ('hi', 'bye', 'nope')
print(list(zip(my_list, your_list, their_list)))
print(my_list)

# reduce:
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))  # 0 = initial accumulator

# lambda functions
# for functions that you just need to use once and are anonymous

my_list = [1, 2, 3]
print(list(map(lambda item: item * 2, my_list)))

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc + item, my_list, 0))

# Be careful this can be confusing

# Square
my_list = [5, 4, 3]
print(list(map(lambda item: item ** 2, my_list)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

# list, set, dictionary comprehensions
# my_list = [param for param in iterable]
# list comprehension
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]
print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# set comprehension  sane as in list

# dict comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict1 = {key: value ** 2 for key, value in simple_dict.items()}
my_dict2 = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
my_dict3 = {key: key*2 for key in [1, 2, 3]}
print(my_dict1)
print(my_dict2)
print(my_dict3)

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)