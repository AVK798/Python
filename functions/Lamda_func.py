s = lambda x: x /x

print(s(45))

# Sort list of dicts by a field
people = [
{"name": "Alice", "age": 30},
{"name": "Bob", "age": 25},
{"name": "Carol", "age": 35},
]
by_age = sorted(people, key=lambda p: p["age"])
for p in by_age:
 print(p["name"], p["age"])
# Bob 25 / Alice 30 / Carol 35
