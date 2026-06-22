# Creating sets
set1={1,2,34,876,2,35,223,445,67,85,2,34,4,1,2}
print(set1)
print(len(set1))

# From a list (removes duplicates)
list=[1,2,3,4,2,1,5,6,7,5,4,7,8,]
unique=set(list)
print(unique)

# Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B) # Union: {1,2,3,4,5,6,7,8}
print(A & B) # Intersection: {4, 5}
print(B - A) # Difference: {1, 2, 3}
print(A ^ B) # Symmetric: {1,2,3,6,7,8}

set1.add("Mango")
print(set1)
#set1.remove("apple")
set1.discard("apple")