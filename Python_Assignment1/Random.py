#Write a Python program to select an item randomly from a list.

import random

l=[]
lucky=[]

for i in range(1,51):
    l.append(i)
    
for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)
    
print(l)
print(lucky)