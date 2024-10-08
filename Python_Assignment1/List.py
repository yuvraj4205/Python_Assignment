'''Write a Python function to get the largest number, smallest num and sum
of all from a list.'''

def listofnum(numbers):
    if not numbers:
        return None,None,0
    
    largest=max(numbers)
    smallest=min(numbers)
    sumoflist=sum(numbers)
    
    return largest,smallest,sumoflist

numbers=[23,45,61,89,0]
largest,smallest,sumoflist=listofnum(numbers)
print("Largest :",largest)
print("Smallest :",smallest)
print("Sum :",sumoflist)