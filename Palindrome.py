n=int(input())
b=0
m=n
while(n!=0):
    a=n%10
    b=b*10+a
    n=n//10
if m==b:
    print(True)
else:
    print(False)