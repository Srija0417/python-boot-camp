#perfect number
n=int(input())
o=n
c=0
for e in range(1,n):
    if n%e==0:
        c=c+e        
if c==o:
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")    
