str1 = input("Enter the input to check the palindrome: ")

is_palindrome = True
n = len(str1)

for i in range(n):
    if str1[i] != str1[n - i - 1]:
        is_palindrome = False
        
if is_palindrome == False:
    print("The input ", str1, " is not a palindrome")
else:
    print("The input", str1, "is a palindrome")