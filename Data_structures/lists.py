empty=[]

lst = [24, "Name","DOB", 1998]

print(lst[0])

#mutable
lst[0] = 10
print(lst)

# list methods


lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(lst.append(7)) # Add to end: [3,1,4,1,5,9,2,6,7]
print(lst.insert(0, 0)) # Insert at index: [0,3,1,4,1,5,9,2,6,7]
print(lst.extend([8, 9])) # Add multiple: [..., 8, 9]
print(lst.remove(1) )# Remove first occurrence of 1
print(lst.pop() )# Remove & return last: 9
print(lst.pop(0) )# Remove & return at index 0
print(lst.sort() )# Sort in-place
print(lst.sort(reverse=True) )# Sort descending
print(lst.reverse()) # Reverse in-place
print(lst.index(5)) # Find index of 5
print(lst.count(1) )# Count occurrences of 1
print(lst.copy() )# Shallow copy
print(lst.clear() )# Empty the list


# Useful built-in functions
nums = [4, 2, 9, 1, 7]
print(len(nums)) # 5
print(sum(nums)) # 23
print(min(nums)) # 1
print(max(nums)) # 9
print(sorted(nums)) # [1, 2, 4, 7, 9] (returns new list)


# list Comprehensions. #


# Syntax: [expression for item in iterable if condition]
# Basic
squares = [x**2 for x in range(1, 11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# With filter
evens = [x for x in range(20) if x % 2 == 0]
print(evens) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# String manipulation
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper) # ["HELLO", "WORLD", "PYTHON"]
# Nested comprehension (flatten matrix)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [n for row in matrix for n in row]
print(flat) # [1, 2, 3, 4, 5, 6, 7, 8, 9]