#positional arguments -  order matters
def num(add, sub):
    return add * sub

print(num(5, 4))

# keyword parameters - order doesn't matter
def  exp( add=5, sub=10):
    print(add * sub)

#Default parameter values
def connect(host, port=5432, ssl=True):
 print(f"Connecting to {host}:{port} (SSL={ssl})")
connect("localhost") # port=5432, ssl=True
print(connect("prod.db.com", 3306, False)) # override all

# 4. *args — variable positional arguments (tuple)
def add(*numbers):
 return sum(numbers)
print(add(1, 2)) # 3
print(add(1, 2, 3, 4, 5)) # 15
# 5. **kwargs — variable keyword arguments (dict)

def args(**list):
   for key,value in list.items():
      print(f'{key}:{value}')

args(name="avk")
