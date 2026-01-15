# Generators

# A generator function in Python is defined using the def keyword like a regular function, but it uses yield instead of return to produce values one at a time. Calling it returns a generator object (an iterator), which pauses execution at each yield and resumes from there on the next request.

# In Python, the yield keyword transforms a function into a generator, allowing it to produce a sequence of values lazily—one at a time—rather than computing and returning them all at once. This pauses execution after yielding a value, saves the function's state (like local variables), and resumes from that point on the next call, making it memory-efficient for large or infinite sequences.


# def generator_func(num):
#     for i in range(num):
#         # print(i)
#         yield (i)


# for item in generator_func(20):
#     print(item)

# ------------------------------


# def toy_counter():
#     toy = 1
#     while True:  # Forever!
#         yield toy
#         toy += 1


# box = toy_counter()
# print(next(box))  # Gives 1, pauses
# print(next(box))  # Gives 2, from where it stopped!
# print(next(box))


# --------------------------


# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator) #return the location in memory
#             print(next(iterator)) #return the value
#         except StopIteration:
#             break

# special_for([6,7,8])

# ------Creating Generator using class-------------


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(1, 100)
for i in gen:
    print(i)
