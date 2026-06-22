def name(tell):
    """ Return a greeting message"""
    return f"Hello, {tell}"

print(name("AVK"))

# Function with no return value returns None

def set(char='-', length=20):
    print(char * length)

set("*", 10)