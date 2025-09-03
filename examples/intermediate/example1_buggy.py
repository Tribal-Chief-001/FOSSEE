# Logic error in list manipulation
numbers = [1, 2, 3, 4, 5]
squared = []
for n in numbers:
    squared.append(n*n)
squared.pop()  # Bug: Removes last element accidentally
print("Squares:", squared)
