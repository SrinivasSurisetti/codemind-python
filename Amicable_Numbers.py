a=int(input())
b=int(input())
s=x=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%j==0:
        x+=j
if (x==a) and (s==b):
    print("Amicable")
else:
    print("Not Amicable")