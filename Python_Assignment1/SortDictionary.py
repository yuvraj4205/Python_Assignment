#Write a Python script to sort (ascending and descending) a dictionary by value.

dict_example = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1, 'elderberry': 6}

sorted_dict_ascending = sorted(dict_example.items(), key=lambda x: x[1])
print("Sorted dictionary in ascending order:")
for key, value in sorted_dict_ascending:
    print(f"{key}: {value}")

sorted_dict_descending = sorted(dict_example.items(), key=lambda x: x[1], reverse=True)
print("\nSorted dictionary in descending order:")
for key, value in sorted_dict_descending:
    print(f"{key}: {value}")