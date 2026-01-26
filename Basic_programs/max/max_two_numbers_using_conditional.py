a = float(input("Enter a: "))
b = float(input("Enter b: "))

if a > b:
    res = a
else:
    res = b
    
print("The Maximum value between a = " + str(a) + " and b = " + str(b) + " is " + str(res))