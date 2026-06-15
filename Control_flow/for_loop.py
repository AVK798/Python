#interate a list
list=["apple","grape","banana"]

for i in list:
    print(i)

#range

for s in range(5):
    print(s, end='*')
    break

#range(start, stop, step)
for n in range(1,20,3):
    print(n, end=" ")

# iterate a string
for c in "python":
    print(c, end=' ')

#enumerate() — index + value together

tech=["Go","java","nodejs","nginx"]

for index, skill in enumerate(tech):
    print(f"{index} : {skill}")

#zip() — iterate multiple iterables in parallel
name=["avk","vk","av"]
score=[20,30,40]
grades=["A","B","C"]

for names,scores,grade in zip(name,score,grades):
    print(f"{names} : {scores} ({grade})")