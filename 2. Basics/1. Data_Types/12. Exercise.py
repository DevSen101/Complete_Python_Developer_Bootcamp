# Write a program to calculate your age by giving DoY.

# name = input('What is your name?\n')
# birth_year = input('Write your birth\'s year\n')
# age = 2026 - int(birth_year)
# print(f'Hii {name}. Your age is {age}.')


# ------------------------------------------------------
# Write a program for password checker

username = input("Write your Name: \n")
password = input("Write your password: \n")
password_length = len(password)
hidden_password = '*' * password_length

print(
    f"Hii {username}. Your password {hidden_password} is {password_length} letters long."
)
