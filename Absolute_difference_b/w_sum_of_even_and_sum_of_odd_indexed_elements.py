n=int(input())
ar = list(map(int,input().split()))
a,m=[],[]
for i in range(n):
    if i%2==0:
        a.append(ar[i])
    else:
        m.append(ar[i])
e=sum(a)
o=sum(m)
print(abs(e-o))