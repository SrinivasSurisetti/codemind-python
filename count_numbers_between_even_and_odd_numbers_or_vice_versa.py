n=int(input())
ls=list(map(int,input().split()))
c=0
c_=0
for i in range(1,n-1):
    if ls[i]%1==0:
        if ls[i-1]%2==1 and ls[i+1]%2==0:
            c+=1
for i in range(1,n-1):
    if ls[i]%1==0:
        if ls[i-1]%2==0 and ls[i+1]%2==1:
            c+=1
print(c+c_)