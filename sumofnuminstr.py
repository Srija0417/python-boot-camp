#hello123
#output:6
n="hello123"
s=0
'''for e in n:
    if e.isnumeric():
        s=s+int(e)
print(s)  
'''
c="0123456789"
for e in n:
    if e in c:
        s=s+int(e)
print(s)        

