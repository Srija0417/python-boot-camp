n=list(map(int,input().split(" ")))
r=[]
for e in range(0,len(n)):
    r.append(n[len(n)-1-e])
print(*r)    