def digSum(n):
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
       return (n % 9)
# def sing(n):
#     sum = 0
#     while(n>0 and sum>9):
#         if n==0:
#             n=sum
#             sum=0
#         else:
#             x=n%10
#             sum =sum+x
#             n/=10
#         return sum
n=int(input())
print(digSum(n))