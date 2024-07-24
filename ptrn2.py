'''# print upper triangular matrix
lower triangular matrix
rombus
paralellogram
number piramid
   1
  212
 32123
 .   .
 .   .
 .   .

#
# '''
n=int(input())
c=n
for e in range(0,n):
    print(" "*e*2+"* "*(c-e))
for e in range(1,n+1):
    print("* "*e)    
    