vowels=['a','e','i','o','u']
words='Programming'
count=0

for char in words:
    if char in vowels:
        count+=1
        #count=char + count

print(count)