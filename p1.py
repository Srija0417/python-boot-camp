#password verifier
'''mr.x is tring to create a new password to his insta acc 
these are required conditions for creating a new password
1.minimum length is 8 max is 15
2.@,/ are must included in a password
3.no spaces are allowed
4.only alpha numerics afe allowed
you are supossed to print weak if length is exact 8
if length if 8 to 12 print medium
if length if 12 to 15 print string'''
p=input()
l=len(p)
c=0
if ("@" in p) and ("/" in p) and (" "not in p):
    c=c+1
if (15<l<8) or c<0 :
    print("follow the conditions")
elif l==8:
    print("weak")
elif 8<l<=12:
    print("medium length")
elif 12<=l<=15:
    print("strong")                