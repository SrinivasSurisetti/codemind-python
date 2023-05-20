(a,b) = map(int,input().split())
x=max(a,b)
while (1):
    if x%a==0 and x%b==0:
        print(x)
        break
    else:
        x+=1