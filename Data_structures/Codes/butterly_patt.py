n=9
j=5
for i in range(1,j+1):
    print(" "*(j-i))
    print("*"*i,end='')
for i in range(1,(j+1)-1):
    print(" "*i)
    print("*"*(j-i),end='')
for i in range(1,j+1):
    print("*"*i)
    print(" "*(j-i),end='')
for i in range(1,(j+1)-1):
    print("*"*(j-i))
    print(" "*i,end='')