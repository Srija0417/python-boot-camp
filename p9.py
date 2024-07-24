# list the leap years from 2000 to given year input
a=int(input())
for e in range(2000,a+1):
    if e%4==0 and e%100!=0:
        print(e)
