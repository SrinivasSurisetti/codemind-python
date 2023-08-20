n=int(input())
ls=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if ls[i]%2==1:
        if ls[i-1]%2==1 and ls[i+1]%2==1:
            c+=1
print(c)