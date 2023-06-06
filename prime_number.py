def p(n):
    if n<=1:
        return 'not a prime'
    for i in range(2,n//2):
        if n%i==0:
            return 'not a prime'
    return 'prime'
print(p(int(input())))