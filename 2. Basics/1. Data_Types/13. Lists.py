# Lists - are like an Array as we have in diff programming language. it's a data structure where we can store any type of data in sequence and access by their index.

# list = [1, 2, "Toy", True, 3.5, "Avengers"]
# print(list[1])

amazon_cart = ["Notebooks", "Sunglasses", "Grapes", "Toys"]
# print(amazon_cart)
amazon_cart[0] = "Laptop"
# print(amazon_cart)
new_cart = amazon_cart
# print(new_cart)

new_cart[0] = "Mac"
# print(amazon_cart)
# print(new_cart)
# In Python, lists are mutable and assignment copies references, not values, so modifying one reference affects all references pointing to the same object.


# # Matrix - matrix are lists inside lists. or Multidimensional array

matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# print(matrix[0][2])
# print(matrix[2][1])


# ---------List Methods---------------

# basket = [1, 2, 3, 4, 5, 6, 10, 12, 3, 1]
# print(basket)

# copy  (imp)
# new_list = basket.copy()
# print(new_list)

# (1) add
# print(basket.append(100))  #it will modify the list not create new.
# print(basket)              #this is modified one.

# (2) insert
# new_list = basket.insert(5, 7)
# print(basket)
# print(new_list)

# (3) extend
# new_list = basket.extend([100, 101])
# print(basket)
# print(new_list)

# (4) pop
# print(basket.pop())   #return pop item
# print(basket.pop(2))    #return pop item at given index

# (5) remove
# new_list = basket.remove(5)
# print(basket.remove(5))
# print(basket)

# (6) clear
# basket.clear()
# print(basket)

# (7) index - return index no of element
# print(basket.index(4))

# (8) in - return bool by search
# print(4 in basket)
# print('in' in 'I lives in Gwalior')

# (9) count - count the element existance
# print(basket.count(5))

# (10) sort
# print(basket.sort())
# print(sorted(basket)) # return a new list

# (11) reverse
# basket.reverse()
# print(basket)

# ---------Common List Pattern--------------------
basket = ["a", "b", "c", "l", "i", "e", "f", "g", "h", "d", "l", "k", "j"]
basket.sort()
basket.reverse()
# print(basket[:])
# print(basket)

# range
# print(range(1,100))
# print(list(range(1,100)))

# join
sentence = '-'
# new_sentence = sentence.join('Hii there Dev here')
new_sentence = '-'.join('Hii there Dev here')
# print(new_sentence)

# ----------List Unpacking-------------------------

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
