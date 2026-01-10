# String indexes = with the help of it. we can access any part of our strings

selfish = "12345678910"
# # INDEX  0123456789

# # Access element of index no.
# print(selfish[5])

# # [start:stop]
print(selfish[0:9])

# # [start:stop:stepover]
# print(selfish[0:11:2])

# # Brainstorming
# print(selfish[1:])
# print(selfish[:6])
# print(selfish[-1])
# print(selfish[::-1])


# -------------------------
# String Immutability - string can't be changed by index we need to reassign them.
# string = '0123456'
# string[0] = '1'
# print(string)
# will give an type error