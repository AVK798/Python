tup =(10, 30)

#tup.append(40)
tup1=(42,)
print(tup1)

# Parentheses are optional (packing)
no_paranthsis=10,20,30
print(type(no_paranthsis))

# unpacking
x ,y = tup
print(f'{x}:{y}')

# extended unpacking
z, *r=no_paranthsis
print(r)