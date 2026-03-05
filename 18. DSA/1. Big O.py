''' 
Big O : notation in DSA (Data Structures & Algorithms) is a way to measure how efficient an algorithm is in terms of time and space as the input size grows.


1. Big O (O) – Upper Bound (Worst Case)
   Tells the maximum time an algorithm can take.
   “Algorithm will never be slower than this”

2. Big Omega (Ω) – Lower Bound (Best Case)
   Tells the minimum time an algorithm will take.
   “Algorithm will take at least this much time”

3. Big Theta (Θ) – Tight Bound (Average / Exact Growth)
   Describes both upper and lower bounds
   “Algorithm grows exactly like this”

In list of [1,2,3,4,5,6,7] finding 1 , 4 , 7 is O, Ω, Θ.

----------------------------------------------------------  '''

# (1) O(n) :- where the number of operations is equal to numbers of n. its propotional in graph.

# def print_items(n):
#  for i in range(n):
#   print(i)

# print_items(10)

# (2) Drop Constant :- No matters how many time n is just drop the constant.


# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)   

# print_items(10)

# (3) O(n^2) :-

def print_items(n):
   for i in range(n):
     for j in range(n):
       print(i, j)

print_items(5)