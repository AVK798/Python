# strings are immutable meaning - we can change or define it in mutiple ways

single='Name'
double="Address"
multiple="""Location"""

print(single)
print(double)
print(multiple)


# concatinate & f strings

full = "hello" + " " + "World !"
Name, age= "AVK", 25
print(f"my Name is{Name}" + " " + "and the age is {age}")

# Raw strings
path=r"c:/programfiles/java"
print(path)
