#wrire a code tp print all the capital letters in a given Strng
n=input()
s=""
for e in n:
    if 65<=ord(e)<=90 :
        s=s+e
print(s)
d=""
for e in n:
    if 97<=ord(e)<=122:
        d=d+e
print(d)        