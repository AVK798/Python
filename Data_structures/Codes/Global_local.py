x=5
def loc():
    global x
    x=15
    y=20
    print("x=%d, y=%d"%(x,y))

loc()
print(x)