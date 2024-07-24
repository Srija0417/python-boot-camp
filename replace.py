#remove al the bracets from the given algibric expression
n=input()
l=""
for e in n:
    if e =="(":
        e.replace("(","")
    elif e==")":    
        e.replace(")","")
    else: 
        l=l+e          #((srija)123)
print(l,end=(" "))     # srija123  

