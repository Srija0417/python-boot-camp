n=int(input())
for i in range (n):
    for j in range(0,n):
        if(i==1 and j==1):
            print("o",end="")
        elif(i+j==2):
            print("x",end="")   
    print( )  