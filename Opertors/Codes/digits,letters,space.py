strng="Name 2344 4234$"
letters=0
digit=0
space=0

for c in strng:
    if c.isalpha():
        letters+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1

print(f'{letters}')
print(f'{digit}')
print(f'{space}')

