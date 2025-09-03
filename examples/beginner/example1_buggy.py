# Off-by-one error in a loop
numbers = [1, 2, 3, 4, 5]
total = 0
for i in range(len(numbers)):
    total += numbers[i+1]  # Bug: IndexError
print("Sum is:", total)
