n=int(input())
s=0
m=n
while n!=0:
    s=(s*10)+n%10
    n//=10
if s==m:
    print(True)
else:
    print(False)