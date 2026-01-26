p = float(input("Enter the principal amount: "))
t = int(input("Enter the time (in months): "))
r = float(input("Enter the rate of intrest (in %): "))

def simple_intrest(p, t, r):
    
    sp = (p * t * r)/(100 * 12)
    
    return sp
    
print("Simple Intrest is " + str(simple_intrest(p, t, r)))