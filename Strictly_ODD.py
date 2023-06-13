n=int(input())
ar = list(map(int,input().split()))
a,b=0,0
for i in range(n):
    if ar[i]%2==1 and i%2==1:
        a+=1
for i in range(n):
    if i%2==1:
        b+=1
if a==b:
    print(True)
else:
    print(False)