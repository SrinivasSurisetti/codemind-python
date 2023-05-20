n = int(input())
s=0
a = list(map(int,input().split()))
for i in range(n):
    if i%2==1:
        s+=a[i]
print(s)