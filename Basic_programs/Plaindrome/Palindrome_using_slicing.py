str1 = input("Enter the input to check the palindrome: ")

if str1 == str1[::-1]:
    print("The input ", str1, " is Palindrome")
else:
    print("The input ", str1, " is not Palindrome")