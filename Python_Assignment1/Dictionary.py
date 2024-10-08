#Write a Python program to convert a list of tuples into a dictionary.

tuples_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

dictionary = {}

for tuple in tuples_list:
    dictionary[tuple[0]] = tuple[1]

print(dictionary)