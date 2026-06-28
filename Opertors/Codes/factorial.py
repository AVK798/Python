n=int(input("enter a number"))
fact=1

for i in range(1,n+1):
    if n < 0:
        print("sorry, we can't find the factorial for this number")
    elif n == 0:
        print(f"Factorail of {n} is 1 ")
    else:
        if n > 0:
            fact=fact*i;
print(f"Fact of {n} is {fact}")