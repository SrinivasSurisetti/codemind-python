def lcm(a,b):
    if a>b:
        mx=a
    else:
        mx=b
    while(True):
        if mx%a==0 and mx%b==0:
            lc=mx
            break
        mx=mx+1
    return lc
(x,y)=map(int,input().split())
print(lcm(x,y))