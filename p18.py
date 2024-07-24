#sum of the even digits
k=int(input())
s=0
while k>0:
    r=k%10
    if r%2==0:
        s=s+ r
    k=int(k/10)
print(s)    

