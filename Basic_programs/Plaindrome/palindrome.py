str1 = "Sas"

str2 = ""

n = len(str1)

for i in range(n):
    #if str1[i] == str1[n - i - 1]:
    str2 = str2 + str1[n - i - 1]
    
print(str2)

if str1 == str2:
    print("The input: ", str1, " is Palindrome")
    
else:
    print("The input: ", str1, " is not Palindrome")
