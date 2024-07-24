n=input()
for e in n:
    if (ord(e)==40 or ord(e)==41 or ord(e)==91 or ord(e)==93 or ord(e)==123 or ord(e)==125):
        pass
    else:
        print(e,end="")
