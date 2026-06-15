s = "Python"
# P y t h o n
# 0 1 2 3 4 5 (positive index)
# -6 -5 -4 -3 -2 -1 (negative index)
print(s[0]) # P
print(s[-1]) # n
print(s[0:3]) # Pyt (start:stop, stop excluded)
print(s[2:]) # thon (from index 2 to end)
print(s[:4]) # Pyth (from start to index 4)
print(s[::2]) # Pto (every 2nd character)
print(s[::-1]) # nohtyP (reversed!)

is_valid = True
is_empty = False
# Booleans are subclasses of int
print(int(True)) # 1
print(int(False)) # 0
print(True + True) # 2
# Truthy / Falsy values
print(bool(0)) # False
print(bool("")) # False
print(bool([])) # False
print(bool(None)) # False
print(bool(42)) # True
print(bool("hello")) # True
print(bool([1])) # True