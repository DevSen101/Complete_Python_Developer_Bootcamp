# Built in functions - python provides us some built in function(refer to python official documents) there are more than 50

quote = "hardwork beats talent when talent doesn't work hard"
# print(quote)

# print(len(quote))
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('work'))
# print(quote.replace('talent', 'luck'))

print(quote)
# This will print same string as we have at starting. strings are immutable we can't modify them just create or destroy. We can assign them in other variable like
quote_2 = quote.replace("talent", "luck")
print(quote_2)