#replace the elements with average of max and min elements

'''list=list(map(int,input().split(" ")))
g=list[0]
for e in range(1,len(list)+1):
    if e+1>len(list)+1:
        break

    if e+1<len(list) and list[e]<list[e+1] :
        g=list[e+1]
print(g)        
s=list[0]
for e in range(1,len(list)+1):
    if e+1>len(list)+1:
        break

    if e+1<len(list) and list[e]>list[e+1] :
        s=list[e+1]
print(s)
sum=g+s
avg=sum/2
for d in range(0,len(list)):
    list[d]=avg
print(*list,end=" ")  '''  

mylist=list(map(int,input().split(" ")))
max=mylist[0]
for i in range(len(mylist)):
    if(mylist[i]>max):
       max=mylist[i]
       
print(max)
min=mylist[0]
for i in range(len(mylist)):
    if(mylist[i]>max):
      min=mylist[i]
print(min)
s=max+min
avg=s/2
print(avg)
''' find evev or odd
find greatest of 3
fins sum of all elements in array
find peak element in an array
find mAX element in an array
find 2nd max element in array
reverse an array without using building functions
find the sum of sqrs of given number
find the sum of even and sum of odd digits
check whether the given number is palindrome or not(original=reverse)
write a program to print first n febnocci series



'''