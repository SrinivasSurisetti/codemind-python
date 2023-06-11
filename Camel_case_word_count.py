# s=input()
# c=0
# for i in  range(1,len(s)+1):
#     if (s[i].supper()):
#         c+=1
# print(c)

def countWords(str):
    count = 1
    for i in range(1, len(str) - 1):
        if (str[i].isupper()):
            count += 1
 
    return count
 
# Driver code
str = input()
print(countWords(str))