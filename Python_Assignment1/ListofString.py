'''Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.'''

strings=["abc","aba","xyz","xyx","abcd","cdc"]
count=0

for string in strings:
    if len(string)>=2 and string[0]==string[-1]:
        count+=1

print("Number of strings with length 2 or more and first and last character same :",count)