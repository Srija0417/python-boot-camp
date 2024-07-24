#print all the vowels folling by consonents
n=input()
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
f=[]
s=[]
for e in n:
    if e in v:
        f.append(e)
    elif e in c:
        s.append(e)
print(*f+s)