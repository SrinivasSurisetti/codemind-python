# import math
# n=int(input())
# c=0
# for i in range(2,int(math.sqrt(n))+1):
#     if n%i==0:
#         c+=1
# if c==0:
#     print("prime")
# else:
#     print("not a Prime")

import math

def primeCheck(x):
    sta = 1
    for i in range(2,int(math.sqrt(x))+1): # range[2,sqrt(num)]
        if(x%i==0):
            sta=0
            print("not a prime")
            break
        else:
            continue
    if(sta==1):
        print("prime")
        return sta

num = int(input())
ret = primeCheck(num)