'''0-9=48-57
A-Z=65-90
a-z=97-122
'''
'''print(ord("D"))
print(chr(68))
'''
#check how many vowels are there in a string
#METHOD-1
n=input()
c=0
for e in n:
    if e=="a" or e=="e"or e=="i"or e=="o" or e=="u":
        c=c+1
print(c)

#METHOD-12
n=input()
v=["a","e","i","o","u"]
c=0
for e in n:
    if e in v:
        c=c+1
print(c)       

