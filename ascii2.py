n=input()

s=0
for e in n:
    if (48<=ord(e)<=58):
        s=s+int(e)
print(s)        

'''0-9=48 to 57
A-Z=65-90
a-z=97-122'''
