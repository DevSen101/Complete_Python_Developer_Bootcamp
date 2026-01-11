# conditional logic statements

# (1) if (if condition is true run this ignore rest..)

is_licenced = False
# is_major = True
is_major = False

# if is_major:
#  print('You can drive')

# (2) else (if all conditions are fail run this)

# if is_major:
#  print('You can drive')
# else:
#  print('You can\'t drive')

# (3) elif

# if is_major:
#     print("You are old enough to drive")
# elif is_licenced:
#     print("You can drive now")
# else:
#     print("You are under age")

# print("OkOK")

# (4) and (and hates false)
if is_major and is_licenced:
    print("Both are true")

# (5) or (or loves true)
if is_major or is_licenced:
    print("Any one is true")
