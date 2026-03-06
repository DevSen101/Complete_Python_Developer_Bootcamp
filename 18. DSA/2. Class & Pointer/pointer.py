# Pointer - refrence to memory address of variable.


num1 = 11
num2 = num1

print("Before num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

# refrence to same memory location.
print(f"num1 points to: ", id(num1))
print(f"num2 points to: ", id(num2))

# Let's check what happen when we change num2, will it affect num1.

num2 = 22

print("After num2 value is updated:")
print("num1 = ", num1)
print("num2 = ", num2)

# refrence to same memory location.
print(f"num1 points to: ", id(num1))
print(f"num2 points to: ", id(num2))

# Integers are immutable it will not change the value of num1 or num2 will be assign to 22

# -------------------------------------------

# Let's try with Dictionery.

dict1 = {"value": 11}
dict2 = dict1

print("Before value is updated: ")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"dict1 points to = {id(dict1)}")
print(f"dict2 points to = {id(dict2)}")

dict2['value'] = 22

print("After value is updated: ")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"dict1 points to = {id(dict1)}")
print(f"dict2 points to = {id(dict2)}")

# here both dictonery value will be updated. memory location will be same.