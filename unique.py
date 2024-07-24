#print the unique char in a string
n=input()
c=[]
for e in n:
    if e not in c:
        c.append(e)
print(*c)        