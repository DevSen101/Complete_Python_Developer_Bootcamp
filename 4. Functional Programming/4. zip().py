# zip()

my_list = [1,2,3]
your_list = (1,2,3)
their_list = [4,5,6]
our_list = (7,8,9,10)

print(list(zip(my_list, their_list)))
print(list(zip(my_list, our_list)))
print(list(zip(my_list, range(2))))
print(list(zip('abcdefg', range(7))))
print(my_list)