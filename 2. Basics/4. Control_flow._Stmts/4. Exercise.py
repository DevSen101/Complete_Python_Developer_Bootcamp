# (1) Make a GUI for list.

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# fill = "*"
# empty = " "
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end=empty)
#         else:
#             print(empty, end=empty)
#     print(" ")


# (2) Check the duplicates in list

some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
