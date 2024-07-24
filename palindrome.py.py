#palindram
n=input()
o=int(n)
s=""
for e in range(0,len(n)):
    s=s+n[len(n)-e-1]
print(s)    
if s==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")       
