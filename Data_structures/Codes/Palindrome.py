Name='level1'

left=0
right=len(Name)-1
while  left < right:
    if Name[left]!=Name[right]:
        print('Not a Palinforme')
        break
    left+=1
    right-=1
else:
    print('Palindrome')
        