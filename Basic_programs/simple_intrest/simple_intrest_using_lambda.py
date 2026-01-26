p = float(input("Enter principal amount: "))
t = float(input("Enter the time (in months): "))
r = float(input("Eneter the rate of intrest (in %): "))

sp = lambda p, r, t : (p * t * r)/(100 * 12)

print("The Simple Intrest is " + str(sp(p, t, r)))