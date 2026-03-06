''' 
Big O : notation in DSA (Data Structures & Algorithms) is a way to measure how efficient an algorithm is in terms of time and space as the input size grows.


1. Big O (O) – Upper Bound (Worst Case) (Most of time we will talk about this)
   Tells the maximum time an algorithm can take.
   “Algorithm will never be slower than this”

2. Big Omega (Ω) – Lower Bound (Best Case)
   Tells the minimum time an algorithm will take.
   “Algorithm will take at least this much time”

3. Big Theta (Θ) – Tight Bound (Average / Exact Growth)
   Describes both upper and lower bounds
   “Algorithm grows exactly like this”

In list of [1,2,3,4,5,6,7] finding 1 , 4 , 7 is O, Ω, Θ.

#----------------------------------------------------------  '''

# (1) O(n) (Proportional):- where the number of operations is equal to numbers of n. its propotional in graph. so O(n)

# def print_items(n):
#  for i in range(n):
#   print(i)

# print_items(10)

# ----------------------------------------------------------

# (2) Drop Constant :- No matters how many time n is just drop the constant.

# here number of operation are n + n = 2n so we will drop constant which is 2 so O(n)

# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)

# print_items(10)

# ----------------------------------------------------------

# (3) O(n^2) (Loop with in a Loop):-

# def print_items(n):
#    for i in range(n):
#      for j in range(n):
#        print(i, j)

# print_items(5)

# ----------------------------------------------------------

# (4) Drop Non-Dominants :-

# def print_items(n):
#    for i in range(n):
#      for j in range(n):
#        print(i, j)

#    for k in range(n):
#      print(k)

# print_items(5)

#  here first two for loops runs O(n^2)  times and last loop runs O(n) times so total O(n^2 + 2) , in case some big number of operation n is nothing in front of n^2 so we will drop the non dominant which is n so O(n^2)

# ----------------------------------------------------------

# (5) O(1) (Constant):-

# def add_items(n):
#  return n + n

# here no matters how many n we are adding complexity is always O(1). this is the most efficient big O.

# ----------------------------------------------------------

# (6) O(log n) (Divide and Conquer):-

# suppose we have [1,2,3,4,5,6,7,8] and we want to find a number. so we just split this thrice (3 times).and we got the number. now this is 2^3 = 8 . this is the concept of log.        log2​(8) = 3 in three operation we got number. let suppose we have to find a number in 2,147,483,648 numbers instead of 8. so log2(2,147,483,648) = 31 . this is the power of log.

# ----------------------------------------------------------

# (7) Different Terms of Inputs :-

# def print_items(a, b):
#  for i in range (a):
#   print(i)
#  for j in range(b):
#   print(j)

# -> So here complexity will we O(a + b)

# def print_items(a, b):
#  for i in range(a):
#   for j in range(b):
#    print(i,j)

# -> So here complexity will we O(a * b)
# ----------------------------------------------------------

# (8) List

#   my_list = [11, 3, 23, 7]

#  Adding & Removing Items from last index of list.
#   my_list.append(15)     -> O(1)
#   my_list.pop()        -> O(1)    (We dont need to do reindexing in both )

#  Adding & Removing Items from strating index of list.
#   my_list.insert(0, 11)  -> O(n)
#   my_list.pop(0) -> O(n)

# Adding and removing items from middle of list will we again O(n), u might be thinking it could be O(1/2n) so in Big O be considered worst case scenerio, also by using simplification rule we frop the constant.

# finding an element in list by Value will be O(n)
# finding an element in list by Index will be O(1)


# ----------------------------------------------------------

# ----------------------------------------------------------
