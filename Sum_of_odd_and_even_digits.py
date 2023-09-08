n=int(input())
ls=list(map(int,input().split()))
ev,od=0,0
for i in range(0,n):
    if i%2==0:
        ev+=ls[i]
    else:
        od+=ls[i]
if (abs(ev-od))==0:
    print("YES")
else:
    print("NO")