my_file = open("G:/Python Code/10. File IO/test.txt")

# To read the file-------
# print(my_file.read())


# To read line by line----------
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# Read the lines by returning list of lines--------
# print(my_file.readlines())

# Close and flush the file---------------
# my_file.close()

# standard way to read file no need to close
# with open("G:/Python Code/10. File IO/test.txt", mode='r+') as my_file:
#  print(my_file.readlines())

# with open("G:/Python Code/10. File IO/test.txt", mode="r+") as my_file:
#     text = my_file.write("Hii its me")
#     print(text)


# pathlib----- learn doc and explore.

# File Error handling

try:
   with open("G:/Python Code/10. File IO/test.txt", mode="r+") as my_file:
      print(my_file.read())
except FileNotFoundError as err:
   print('File doesn\'t found') 
   raise err
except IOError as err:
   print('IO Error')
   raise err     
    
    

