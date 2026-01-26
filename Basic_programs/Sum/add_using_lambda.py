a = int(input("Enter a: "))
b = int(input("Enter b: "))

res = lambda a, b : a + b

print("The addition of a = " + str(a) + ", b = " + str(b) + " is " + str(res(a, b)))