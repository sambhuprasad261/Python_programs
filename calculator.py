"""
Simple Calculator
----------------
A simple calculator program demonstrating functions and user interaction.
This is a mini-project to practice Python basics.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    """Calculate x raised to the power of y."""
    return x ** y

def modulus(x, y):
    """Calculate remainder of x divided by y."""
    if y == 0:
        return "Error: Division by zero!"
    return x % y

def display_menu():
    """Display calculator menu."""
    print("\n" + "=" * 50)
    print("SIMPLE CALCULATOR")
    print("=" * 50)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    print("=" * 50)

def calculate(choice, num1, num2):
    """Perform calculation based on choice."""
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/'),
        '5': (power, '**'),
        '6': (modulus, '%')
    }
    
    if choice in operations:
        func, symbol = operations[choice]
        result = func(num1, num2)
        print(f"\n{num1} {symbol} {num2} = {result}")
        return result
    else:
        print("\nInvalid choice!")
        return None

def run_calculator():
    """Main calculator function."""
    print("Welcome to Simple Calculator!")
    
    while True:
        display_menu()
        
        # Commented out for automated testing
        # In real use, uncomment the following lines:
        """
        choice = input("\nEnter choice (1-7): ")
        
        if choice == '7':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("\nInvalid choice! Please select 1-7.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            calculate(choice, num1, num2)
            
        except ValueError:
            print("\nInvalid input! Please enter numbers only.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        """
        
        # For demonstration purposes, let's run some examples
        print("\nDemonstration mode:")
        print("\nExample calculations:")
        
        # Example calculations
        calculate('1', 10, 5)  # Addition
        calculate('2', 10, 5)  # Subtraction
        calculate('3', 10, 5)  # Multiplication
        calculate('4', 10, 5)  # Division
        calculate('5', 2, 3)   # Power
        calculate('6', 10, 3)  # Modulus
        
        print("\n" + "=" * 50)
        print("To use this calculator interactively:")
        print("1. Uncomment the user input section in the code")
        print("2. Run the program")
        print("3. Follow the menu prompts")
        print("=" * 50)
        
        break  # Exit after demonstration

if __name__ == "__main__":
    run_calculator()
