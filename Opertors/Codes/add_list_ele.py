list1=[1,2,3]
list2=[3,4,5]

list3=list1 + list2
print(list3)


total = [ a+b for a,b in zip(list1, list2)]
print(total)