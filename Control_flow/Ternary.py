# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status) # adult
# Nested ternary (use sparingly — readability suffers)
x = 5
label = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(label) # positive