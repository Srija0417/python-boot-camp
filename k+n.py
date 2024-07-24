#find the element that is present in k+n index 
#k=3
#n=2
#input 3 6 8 4 61 2
#output 2

#k=3
#n=4
#80 70 54 36 72
#output=error
k=int(input())
n=int(input())
list=list(map(int,input().split(" ")))
'''if k+n<len(list):
    print(list[k+n])
else:
    print("error") '''
for e in range(0,len(list)):
    print(list[k+n],end=" ")
    break
    