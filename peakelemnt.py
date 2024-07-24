'''n=list(map(int,input().split(" ")))
for e in range(1,len(n)-1):
    if n[e-1]<n[e] and n[e]>n[e+1]:
        print(n[e])'''
#if peak  elements are 2 and should print 2 elements in output
n=list(map(int,input().split(" ")))
peak=0
for e in range(1,len(n)-1):
    if n[e]>n[e-1] and n[e]>n[e+1]:
        peak=e
        print(n[peak])
'''#if peak  elements are 2 
n=list(map(int,input().split(" ")))
peak=0
for e in range(1,len(n)-1):
    if n[e]>n[e-1] and n[e]>n[e+1]:
        peak=e
print(n[peak])'''



