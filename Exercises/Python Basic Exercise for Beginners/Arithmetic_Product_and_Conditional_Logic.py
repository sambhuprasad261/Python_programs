"""
Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

"""

def arth_prod(a, b):
    
    mul = a * b
    add = a + b
    
    if mul <= 1000:
        return mul 
    else:
        return add
        
a = int(input("Enter a: "))
b = int(input("Enter b: "))

out = arth_prod(a, b)

print("The output is", out)