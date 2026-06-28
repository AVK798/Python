count=0
def count_spec(string):
    spc="""! @ # $ % ^ & * ( ) _ + - = { } [ ] : ; " ' < > , . ? / ~ `"""
     
    for i in string:
        if i in spc:
         global count
         count+=1
        
    return count
    
count_spec('rtgpkvmn#$@&()gvdcv')

print(count)

