def ct(n,m):
    if n.count(m)>0:
        return n.count(m)
    else:
        return -1
a=input()
b=input()
print(ct(a,b))