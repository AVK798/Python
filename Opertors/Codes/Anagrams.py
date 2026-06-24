str1='listen'
str2='silent'

str3=str1.replace(" ","").upper()
str4=str2.replace(" ","").upper()

if sorted(str3) == sorted(str4):
    print(True)
else:
    print(False)