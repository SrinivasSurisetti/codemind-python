n=input()
s=[]
for i in n:
    if int(i)%2==1:
        s.append(int(i)*int(i))
for i in s:
    print(i,end="")