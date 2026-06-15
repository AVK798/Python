x,y=10,20

print(x == y)
print( x!=y)
print(x < y)
print(x > y)
print(x <= y)
print(x>= y)

# Chain comparisons (unique to Python!)
age = 12
print(18 <= age < 65) 

# String comparison (lexicographic)
print("apple" < "banana") # True
print("Python" == "python") # False (case sensitive)