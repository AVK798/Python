x = "global" # Global scope
def outer():
 x = "enclosing" # Enclosing scope
 def inner():
  x = "local" # Local scope
  print(x) # local
 inner()
 print(x) # enclosing
outer()
print(x) # global

# global keyword — modify global variable inside function
counter = 0
def increment():
 global counter
counter += 1
increment()
increment()
print(counter) # 2
# nonlocal — modify enclosing scope variable
def make_counter():
 count = 0
 def increment():
  nonlocal count
 count += 1
 return count
 return increment
c = make_counter()
print(c(), c(), c()) # 1 2 3