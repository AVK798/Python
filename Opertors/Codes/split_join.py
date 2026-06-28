str='Once you learn to convert a normal for loop into this pattern'
s1=str.split(" ")
# split the string into list of string
s2=s1[::-1]
print(s2)

s3= " ".join(s2)
print(s3)
# join converts list of string into string