a = float(input("Enter a: "))
b = float(input("Enter b: "))

lst = [a, b]
lst.sort()

print("The Maximum value between a = " + str(a) + " and b = " + str(b) + " is " + str(lst[-1]))