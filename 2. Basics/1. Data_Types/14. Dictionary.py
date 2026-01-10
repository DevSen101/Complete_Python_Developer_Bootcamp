# Dictionary - are the key-value pair, stored as an unordered way in the memory. It's like an Object
dictionary = {"a": [1, 2, 3, 4, 5], "b": True, "c": "Hello"}

dic_2 = dict(v="Vinod")
# print(dic_2)
# print(dictionary['a'][2])

# Note
# a dictionary key should be immutable which will not change, it should be unique if the key is overwritten more than once it will delete previous key-value pair.


# ------------ Dictionary Methods -----------------
# .get() method
# print(dictionary.get("b"))
# make a new key-value pair in case there is no.
# print(dictionary.get("d", 50))


user = {"basket": [1, 2, 3], "greet": "value", "age": 20}

# in - check the existance
# print('basket' in  user)
# print(20 in user)

# .keys()
# print("basket" in user.keys())

# .values()
# print('value' in user.values())

# .items()
# print(user.items())

# .clear() 
# print(user.clear())

# .copy()
# user_2 = user.copy()
# print(user.clear())
# print(user_2)

#.pop() - return the removed value of given key
# print(user.pop('age'))
# print(user)

# .popitem() - returns the last key-value pair
# print(user.popitem())

# .update() - update a key-value pair also add if there is no any
# user.update({'age': 50})
# user.update({'DoB': 2004})
# print(user)