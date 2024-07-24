# print element at particular index
k=int(input())
list=list(map(int,input().split(" "))) 
m=k%len(list)
print(list[m-1])

