num = int(input("number = "))

def fact(num):
    n = 1
    for i in range(1, num + 1):
        n = i * n
    
    return n
    
factorial = fact(num)

print("The Factorial of", num, "is", factorial)