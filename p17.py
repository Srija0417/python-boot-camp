#sum od sqrs of the input
k=int(input())
s=0
while k>0:
    s=s+(k%10)**2
    k=int(k/10)
print(s)    

