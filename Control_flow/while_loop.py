# a=1
# while a < 5:
#  print(a, end='-')
#  a+=1
#do-while pattern (Python has no do-while keyword)
user_input = ""
while True:
 user_input = input("Enter a positive number: ")
 if user_input.isdigit() and int(user_input) > 0:
   print("Valid")
   break
print("Invalid input, try again.")
