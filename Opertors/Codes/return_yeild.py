def add():
    return 10
    return 20

print(add())

####################

def sub():
    yield 10
    yield 20

print(next(sub()))

#######################

def first(n):
    for i in range(1,n+1):
        yield i
    
#for num in first(5):
num=first(5)
print(next(num))
print(next(num))
print(next(num))
print(next(num))