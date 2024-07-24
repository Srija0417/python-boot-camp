#reverse the numbers in a given String
n="hello1234world"
s=""
c="0123456789"
for e in n:
    if e in c:
        s=s+e
print(s)
d=s
for e in d:
    print(d[len(d)-int(e)],end=(" "))  

