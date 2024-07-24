'''gcd of 2 numbers
euclidean algorithm
'''
a=int(input("1st number: "))
b=int(input("2nd number: "))
while b!=0:
    a,b=b,a%b
print("gcd of above 2 numbers is :",a)    