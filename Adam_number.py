n=int(input())
x=n*n
r=0
while n!=0:
    s=n%10
    r=r*10+s
    n//=10
y=r*r
c=0
while y!=0:
    b=y%10
    c=c*10+b
    y//=10
if x==c:
    print(True)
    
else:
    print(False)