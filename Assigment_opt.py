N=5

N+= 5
N -= 6
N *= 7
N /= 8
N //= 9
N %= 10
N **= 2

# Walrus operator

import re
data = "User: Alice, Age: 30"
if m := re.search(r"Age: (\d+)", data):
 print(f"Found age: {m.group(1)}") # Found age: 30