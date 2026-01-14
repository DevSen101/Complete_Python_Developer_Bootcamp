# Functional Programming - is all about separating concern, we separate the data and behavier.

# Pure Function - which is all by his own. in below ex this func dont need anything from outside world for ex if i make new_list to a global var so it will a side effect, or if i write return print(new_list) so again it has a side effect. so idealy we contain everything in the function. but is not always possible.

# new_list = []           side effect
def multiply_by_2(li):
    new_list = []
    for items in li:
        new_list.append(items*2)
    return new_list
    # return print(new_list)          side effect
    
print(multiply_by_2([1,2,3]))