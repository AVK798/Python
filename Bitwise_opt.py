& and
| or
^ XOR
~ not
<< leftshit
>> rightshit


# Precedence: ** > unary > * / // % > + - > comparisons > logical
print(2 + 3 * 4) # 14 (not 20!) — * before +
print((2 + 3) * 4) # 20 — parentheses first
print(2 ** 3 ** 2) # 512 — ** is right-associative: 2**(3**2)=2**9
print(True or False and False) # True — and before or

# When in doubt, use parentheses—they make your code easier to read and avoid precedence mistakes.