n=int(input())
s=0
while n>0:
    s=s+(n%10)**2
    n=int(n/10)
print(s)    