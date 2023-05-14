def am(a):
    if a<0:a=-a
    sqnum=a*a
    temp=a
    c=0
    while(temp!=0):
        c+=1
        temp//=10
    lastdg=sqnum%pow(10,c)
    if lastdg==a:
        return 'Automorphic Number'
    else:
        return 'Not an Automorphic Number'
n=int(input())
print(am(n))