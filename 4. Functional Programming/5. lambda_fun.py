# lambda functions - is a one time anonumous function which run once.without a name
# lambda param: (action want to take on param)

my_list = [1, 2, 3]


def mul_by_2(item):
    return item * 2

print(list(map(lambda item: item*2, my_list)))  #here we dont need mul_by_2 function
