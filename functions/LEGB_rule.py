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