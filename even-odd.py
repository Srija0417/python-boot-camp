n=int(input())
e=0
o=0
while n>0:
    r=n%10
    if n%2==0:
        e=e+r
    else:
        o=o+r
    n=n//10
print(e)
print(o)
print(e+o)


        