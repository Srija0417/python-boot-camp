#amstrong
n=input()
s=0
for e in range(0,len(n)):
    s=s+int(n[e])**len(n)
if s==int(n):
    print(n,"is a amstrong number")
else:
    print(n,"is not a amstrong number")    