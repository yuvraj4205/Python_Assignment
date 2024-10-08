#Write a Python program to remove duplicates from a list.

my_list=[1,2,2,3,4,4,5,6,6,7,8,8,9]

unique_list=[]

for element in my_list:
    if element not in unique_list:
        unique_list.append(element)

print(unique_list)