n=list(map(int,input().split(" ")))
c=0
d=0
s=0
for e in range(len(n)):
    if n[e]%2==0:
        c=c+1
        s=s+n[e]
    else: 
        d=d+1
print(c,d)
print(s//c)