key1 = {"name":"AVK", "age":27, "role":"DevOps"}

print(key1["name"])

key1["age"]=28

print(key1["age"])

#modify
del key1["role"]
print(key1)

# Iteration
for key in key1:
    print(key)
for v in key1.values():
    print(v)
for key,vlaue in key1.items():
    print(f'{key},{vlaue}')

# dict comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1:1, 2:4, 3:9, 4:16, 5:25}

even = {x: x%2 for x in range(1,5)}
print(even)