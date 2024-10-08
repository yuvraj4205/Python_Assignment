#Write a Python function to check whether a number is perfect or not.

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(12))