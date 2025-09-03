# Recursive factorial with wrong base case
def factorial(n):
    if n == 1:  # Bug: fails for n = 0
        return 1
    return n * factorial(n-1)

print(factorial(0))
