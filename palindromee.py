o=int(input())
k=o
r=""
s=0
while o>0:
    s=o%10
    r+=str(s)
    o=o//10 
if str(k)==r :
    print("palindrome")  
else:
    print("not a palindrome")      
