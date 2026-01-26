n = int(input("Enter the number: "))

def factres(num):
    
    if num < 1:
        return 1
        
    else:
        return num * factres(num - 1)
    
    
print("The factorial of " + str(n) + " is " + str(factres(n)))