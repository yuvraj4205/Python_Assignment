#Write a Python program to map two lists into a dictionary

keys = ['a', 'b', 'c']
values = [1, 2, 3]

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)