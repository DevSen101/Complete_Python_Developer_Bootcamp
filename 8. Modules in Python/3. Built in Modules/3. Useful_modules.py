from collections import Counter, defaultdict, OrderedDict

list = [1,2,3,4,5,6,4,5,6,7,8,9,5,6]
sentence = 'hello everybody my name is ajay and i am ceo of xyz organisation'
# Counter will return a dictionery where key will be item and value will be no of iteration in our collections
# print(Counter(list))
# print(Counter(sentence))

# ---------------

dictionary = defaultdict(lambda: 'does not exist', {'a': 1,'b': 2 })
# print(dictionary['c'])

# -----------------

d = OrderedDict()
d['a'] = 1
d['b'] = 2


d2 = OrderedDict()
d2["b"] = 2
d2["a"] = 1

# print(d == d2)


# ==========================
import datetime

# print(datetime.time(5,20,56))
# print(datetime.date.today())

# --------------------------
from array import array

arr = (array('i', [1,2,3]))
print(arr)