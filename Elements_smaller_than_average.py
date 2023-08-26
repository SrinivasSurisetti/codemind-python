n = int(input())
ar = list(map(int,input().split()))
arr=[]
av=sum(ar)//n
for i in range(0,n):
    if ar[i]<=av:
        arr.append(ar[i])
print(len(arr))