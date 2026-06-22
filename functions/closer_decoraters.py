# A closure is a nested function that remembers and can access variables from its enclosing scope even after the outer function has completed execution.

def outer():
    x = 10
    def inner():
        print(x)
    return inner

# A decorator is a function that takes another function as input, adds additional functionality, and returns a modified function. Decorators are commonly used for logging, authentication, caching, monitoring, retries, and performance measurement.

import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Took {end-start:.2f}s")
    return wrapper

@timer
def backup():
    time.sleep(2)
    print("Backup complete")

backup()