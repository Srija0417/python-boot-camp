arr=list(map(int,input().split(" ")))
e=[]
o=[]
for i in arr:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)    
print("even : ",e)
print("odd : ",o)        
