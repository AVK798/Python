vowels=['a','e','i','o','u']
words='Programming'
count=0

for char in words:
    if char not in vowels:
        count+=1

print(count)