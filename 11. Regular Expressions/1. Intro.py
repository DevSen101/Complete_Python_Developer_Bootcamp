# Regular Expressons - used to check the validations.
import re

string = "search this inside of this text please! please Dev sen"

# print('this' in string)

# a = re.search('this', string)
# print(a.span()) #return index where the string exists.
# print(a.start()) #return starting index no.
# print(a.end())  # return ending index no.
# print(a.group())

# -------------------

# pattern = re.compile("this")
pattern = re.compile("search this inside of this text please")
a = pattern.search(string)  # return first match.
b = pattern.findall(string)  # return list for all matches.
c = pattern.fullmatch(string) # check for complete match
d = pattern.match(string)
# print(a.group())
# print(b)
# print(c)
print(d)

# ------Regular expressions 101-----where we can find all regex in every language