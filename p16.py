#sum of digits
k=int(input())
s=0
'''for e in range(0,len(k)):
    s=s+int(k[e])
print(s)'''
while k>0:
    s=s+(k%10)
    k=int(k/10)
print(s)    



    