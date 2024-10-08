#Write a Python program to find the second smallest number in a list.

numbers = [5, 3, 9, 1, 7, 3, 2]

smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num

if second_smallest == float('inf'):
    print("There is no second smallest number in the list.")
else:
    print("The second smallest number is:", second_smallest)