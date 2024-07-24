#LCM of 2 numbers
a=int(input("1st number: "))
num1=a
b=int(input("2nd number: "))
num2=b
while b!=0:
    a,b=b,a%b
gcd=a    
print("lcm of given numbers is :",int(num1*num2/gcd))  
