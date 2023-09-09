n=int(input())
ar=list(map(int,input().split()))
arr=[]
arrr=[]
for i in range(n):
    if ar[i]!=0:
        arr.append(ar[i])
    else:
        arrr.append(ar[i])
print(*(arr+arrr))