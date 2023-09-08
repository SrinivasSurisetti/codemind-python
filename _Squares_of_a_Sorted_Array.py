n=int(input())
ls=list(map(int,input().split()))
sq=[]
for i in ls:
    sq.append(i*i)
sr=sorted(sq)
print(*sr)