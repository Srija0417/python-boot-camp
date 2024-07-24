f=[]
a=0
f.append(a)
b=1
f.append(b)
sum=1
for e in range(0,10):
    sum=sum+int(f[len(f)-2])
    b=sum
    f.append(sum)

print(*f)    