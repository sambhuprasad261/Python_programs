num = str(int(input("Enter the number: ")))

rev = num[::-1]

if num == rev:
    print(f"Number {num} is a Palindrome number")
else:
    print(f"Number {num} is not a Palindrome number")