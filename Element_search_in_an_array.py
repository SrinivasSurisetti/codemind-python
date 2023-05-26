n=input()
a=list(map(int,input().split()))
s=int(input())
for i in range(len(a)):
    if a[i]==s:
        print(True)
        break
else:
    print(False)