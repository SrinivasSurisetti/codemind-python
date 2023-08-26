n = int(input())
a = list(map(int,input().split()))
ar=[]
arr=[]
for i in range(n):
    if a[i]%2==1:
        ar.append(a[i])
    else:
        arr.append(a[i])
print(*(ar+arr))