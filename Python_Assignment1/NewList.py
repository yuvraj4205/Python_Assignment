'''Write a Python function that takes a list and returns a new list with unique
elements of the first list.'''

def unique_elements(input_list):
    unique_set=set(input_list)
    return list(unique_set)

original_list=[1,2,2,3,4,4,5]
unique_list=unique_elements(original_list)
print(unique_list)