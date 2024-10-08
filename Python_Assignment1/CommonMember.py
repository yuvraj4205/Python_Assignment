'''Write a Python function that takes two lists and returns true if they have
at least one common member.'''

def have_common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

list1=[1,2,3,4]
list2=[3,4,5,6]

if have_common_element(list1,list2):
    print("The lists have at least one common element.")
else:
    print("The lists have no common elements.")