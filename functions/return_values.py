def single(n):
    return n * n

single(4)

def multiple(z):
    return min(z), max(z)

low, high=multiple([1,2,3,76,24,45,2])

print(f'{low}, {high}')


# early return

def div(a,b):
    if b == 0:
        return None
    return a * b

result= div (4,0)
if result is None:
    print("Can't divide the passed values")

