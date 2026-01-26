def add_two_numbers(a, b):
    
    res = a + b
    
    return res

a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = add_two_numbers(a, b)

print("The addition of a = " + str(a) + ", b = " + str(b) + " is " + str(result))