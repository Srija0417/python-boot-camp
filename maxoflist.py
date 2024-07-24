n=list(map(int,input().split(" ")))
max=n[0]
for e in range(0,len(n)):
    if n[e]>=max:
        max=n[e]
print(max)        