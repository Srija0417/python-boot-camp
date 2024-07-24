#if peak is at last of list
n=list(map(int,input().split(" "))):
c=0
for e in range(1,len(n)):
    if n[e]>n[e-1] and n[e]>n[e+1]:
        c=e


