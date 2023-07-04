n=int(input())
a=list(map(int,input().split()))
ar=reversed(a)
for i in ar:
    if i%2==1:
        print(i)
        break