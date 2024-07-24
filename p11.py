#find the maximum element in a given list
list=list(map(int,input().split(" ")))
greatest=list[0]
for e in range(1,len(list)+1):
    if e+1>len(list)+1:
        break

    if e+1<len(list) and list[e]<list[e+1] :
        greatest=list[e+1]
print(greatest)        