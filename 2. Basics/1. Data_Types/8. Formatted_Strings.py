# Formatted strings

name = "Dev"
age = 22

# By type conversion
print("Hii " + name + ". You are " + str(age) + " years old.")  

# By Formatted strings
print(f'Hii {name}. You are {age} years old.')
print("Hii {}. You are {} years old.".format(name, age))
print("Hii {1}. You are {0} years old.".format(name, age))
