#Write a Python program to check whether a list contains a sub list

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [4, 5, 6]

found = False

for i in range(len(main_list) - len(sub_list) + 1):
    if main_list[i:i+len(sub_list)] == sub_list:
        found = True
        break

if found:
    print("The sub list is found in the main list.")
else:
    print("The sub list is not found in the main list.")