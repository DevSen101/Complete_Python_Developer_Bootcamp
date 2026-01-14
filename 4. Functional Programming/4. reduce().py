# reduce()

from functools import reduce

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item + 10


print(reduce(accumulator, my_list, 5))
# print(my_list)
