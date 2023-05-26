n=int(input())
a=list(map(int,input().split()))
x=sum(a)//n
for i in range(n):
    if a[i]==x:
        print(True)
        break
else:
    print(False)