s=0
c=""
list=[]
for e in range(1,101):
    c=c+str(e)
    s=s+e
    print(e,end=" ")
list.append(c)
print(*list)
print(s)

