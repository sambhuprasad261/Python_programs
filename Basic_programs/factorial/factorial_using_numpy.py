import numpy as np

n = int(input("Enter the number: "))

fact = np.prod(range(1, n + 1))

print("The factorial of " + str(n) + " is " + str(fact))