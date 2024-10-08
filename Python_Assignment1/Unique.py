#Write a Python program to get unique values from a list

values = [1, 2, 2, 3, 4, 4, 5, 6, 1]

unique_values = []

for value in values:
    if value not in unique_values:
        unique_values.append(value)

print("Unique values:", unique_values)