n=int(input())
for i in range(n):
    for j in range(0,n):
        if(i<j or i==j):
           print("*",end=" ")
    print(" ")