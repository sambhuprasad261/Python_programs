"""
Loops in Python
--------------
Learn about for loops and while loops for repetitive tasks.
"""

print("=" * 50)
print("FOR LOOP - Iterating through a range")
print("=" * 50)

# Basic for loop
for i in range(5):
    print(f"Iteration {i}")

print("\n" + "=" * 50)
print("FOR LOOP - With start, stop, and step")
print("=" * 50)

# For loop with custom range
for i in range(2, 11, 2):
    print(f"Even number: {i}")

print("\n" + "=" * 50)
print("FOR LOOP - Iterating through a list")
print("=" * 50)

# Iterating through a list
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n" + "=" * 50)
print("FOR LOOP - With index and value")
print("=" * 50)

# Using enumerate to get both index and value
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

print("\n" + "=" * 50)
print("WHILE LOOP")
print("=" * 50)

# Basic while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print("\n" + "=" * 50)
print("WHILE LOOP - User input simulation")
print("=" * 50)

# While loop with condition
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print(f"Sum of numbers 1 to 10: {total}")

print("\n" + "=" * 50)
print("BREAK STATEMENT")
print("=" * 50)

# Using break to exit loop
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"Number: {i}")

print("\n" + "=" * 50)
print("CONTINUE STATEMENT")
print("=" * 50)

# Using continue to skip iterations
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

print("\n" + "=" * 50)
print("NESTED LOOPS")
print("=" * 50)

# Nested loops - multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}", end="  |  ")
    print()  # New line after each row

print("\n" + "=" * 50)
print("LOOP WITH ELSE")
print("=" * 50)

# Loop with else clause (executes if loop completes normally)
for i in range(5):
    print(f"Number: {i}")
else:
    print("Loop completed successfully!")
