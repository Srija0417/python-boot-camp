#check given number is prime number or not
a=int(input())
r=a**0.5
c=0
if a==1:
    print("not a prime number")
for e in range(2,int(r+1)):
    if (a%2==0):
        c=c+1
        break
if c==0:
    print("prime number")    
else:
    print("not prime")    
    
