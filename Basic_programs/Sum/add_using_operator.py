import operator

a = float(input("Enter a: "))
b = float(input("Enter b: "))

print("The addition of two numbers a = " + str(a) + " and b = " + str(b) + " is " + str(operator.add(a, b)))