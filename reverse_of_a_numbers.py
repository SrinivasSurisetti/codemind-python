def revn(n): 
   if n >= 0: 
      return int(str(n)[::-1])
   else:
      return int('-{val}'.format(val = str(n)[1:][::-1]))
# take inputs
num = int(input())
# calling function and display result
print(revn(num))