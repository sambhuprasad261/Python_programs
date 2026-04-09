num = int(input("num = "))

def IsPali(num):
    temp = num
    key = 0
    
    while temp > 0:
        key = temp % 10 + key*10
        temp = temp // 10
    print(key)
     
    return key

res = IsPali(num)

if res ==  num:
    print(f"Yes. given number {num} is palindrome number")
else:
    print(f"No. given number {num} is not palindrome number")