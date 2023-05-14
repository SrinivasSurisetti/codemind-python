(a,b)=map(int,input().split())
for i in range(1,11):
    if a+b+i==21:
        print(i)
        break
else:
    print(-1)