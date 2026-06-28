import time
def logging(func):
    def log():
        start=time.time()
        print("start calculating")
        func()
        end=time.time()
        print(f"Took time is {end-start:.2f}s")
    return log

@logging
def final():
    print("complete")

final()

##########################

def valu():
    x=5
    def fina():
        print(x)

    return fina
tot=valu()
tot()