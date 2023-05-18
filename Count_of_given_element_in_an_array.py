def ct(ar,target):
    c=0;
    for i in ar:
        if i == target:
            c+=1
    return c
n=int(input())
ar=list(map(int,input().split()))
target=int(input())
 
r=ct(ar,target)
print(r)