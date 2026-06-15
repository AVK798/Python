#break, continue, pass, else

# break — exits the loop immediately
for n in range(10):
 if n == 5:
  break
print(n, end=" ") # 0 1 2 3 4
# continue — skips the rest of this iteration
for n in range(10):
 if n % 2 == 0:
  continue
print(n, end=" ") # 1 3 5 7 9
# pass — does nothing; placeholder for empty blocks
for n in range(5):
 pass # will add logic later
# else on a for loop — runs if loop completed WITHOUT break
for n in range(2, 10):
 for factor in range(2, n):
  if n % factor == 0:
    break
 else:
  print(f"{n} is prime", end=" ") # 2 3 5 7