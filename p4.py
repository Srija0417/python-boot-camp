#sort a list which 1st half should be acsending and 2nd half should be decending
n=list(map(int,input().split(" ")))
n.sort()
l=[]
a=[]
h=int(len(n)/2)
for e in range(h,len(n)):
    l.append(n[h-e-1])
for e in range(0,h):
    a.append(n[e])
print(*a+l)




