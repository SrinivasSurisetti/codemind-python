n=int(input())
s=0
m=n
while n!=0:
   x=n%10 
   s=(s*10)+x
   n//=10
if m==s:
    print(True)
else:
    print(False)