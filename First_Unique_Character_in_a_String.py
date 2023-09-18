s=input()
c=0
for i in range(0,len(s)):
    if s.count(s[i])==1:
        c+=1
        print(i)
        break
if c==0:
    print(-1)