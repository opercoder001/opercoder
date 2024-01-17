a=input(">>> ")
c=len(a)
ls=[]
for i,v in enumerate(a):
    c=len(a)-i-1
    d=v+'0'*c
    ls.append(d)
eee="+".join(ls)
print(eee)