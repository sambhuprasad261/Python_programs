income = int(input("Enter income: "))

tax = 0

if income >= 10000:
    tax = 0
    income = income - 10000
    
    if income >= 10000:
        tax = tax + 10000 *(10/100)
        income = income - 10000
        
        if income > 0:
            tax = tax + income *(20/100)
        
    else:
        pass
        
else:
    tax = 0
    
    
print(f"Total income tax to pay is {tax}")