#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

my_dict = {}
for i in range(1, 16):
    my_dict[i] = "Value " + str(i)

print(my_dict)