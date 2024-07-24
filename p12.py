#find the minimum element in a given list
list=list(map(int,input().split(" ")))
s=list[0]
for e in range(1,len(list)+1):
    if e+1>len(list)+1:
        break

    if e+1<len(list) and list[e]>list[e+1] :
        s=list[e+1]
print(s)        