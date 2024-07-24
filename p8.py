# list out prime numbers from start number to stop number
a=int(input("star: "))
b=int(input("stop: "))
for e in range(a,b+1):
    for d in range(2,e):
        if e%d==0:
            break
    else:
        print(e)    

