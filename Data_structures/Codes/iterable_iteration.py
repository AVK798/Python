list=[1,4,54,54,3]
ls=iter(list)
print(next(ls))
print(next(ls))

#####################

def line():
    x=[1,3,4,5,6,5]

    yield x

ln=line()
print(next(ln))