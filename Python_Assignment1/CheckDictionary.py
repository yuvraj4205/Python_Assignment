#Write a Python script to check if a given key already exists in a dictionary.

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

key_to_check = 'age'

if key_to_check in my_dict:
    print("The key",key_to_check,"exists in the dictionary.")
else:
    print("The key",key_to_check,"does not exist in the dictionary.")