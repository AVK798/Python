strng='Python Programming'
print(strng[::-1])

final=''
##################
for i in strng:
    final= i + final
print(final)

##################
print("".join(reversed(strng)))