t=int(input())
for i in range(t):
    x=int(input())
    def fact(x):
        if x==1 or x==0:
            return 1
        else:
            return x*fact(x-1)
    print(fact(x))
        
        