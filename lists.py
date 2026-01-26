"""
Lists in Python
--------------
Learn about list operations, methods, and manipulations.
"""

print("=" * 50)
print("CREATING LISTS")
print("=" * 50)

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

print("\n" + "=" * 50)
print("ACCESSING LIST ELEMENTS")
print("=" * 50)

# Accessing elements by index
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

print("\n" + "=" * 50)
print("LIST SLICING")
print("=" * 50)

# Slicing lists
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")
print(f"First 5: {numbers[:5]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle elements: {numbers[3:7]}")
print(f"Every other element: {numbers[::2]}")

print("\n" + "=" * 50)
print("MODIFYING LISTS")
print("=" * 50)

# Modifying list elements
colors = ["red", "green", "blue"]
print(f"Original: {colors}")

colors[1] = "yellow"
print(f"After modification: {colors}")

print("\n" + "=" * 50)
print("ADDING ELEMENTS")
print("=" * 50)

# Adding elements to list
animals = ["cat", "dog"]
print(f"Original: {animals}")

# Using append to add one element
animals.append("bird")
print(f"After append: {animals}")

# Using extend to add multiple elements
animals.extend(["fish", "rabbit"])
print(f"After extend: {animals}")

# Using insert to add at specific position
animals.insert(1, "hamster")
print(f"After insert at index 1: {animals}")

print("\n" + "=" * 50)
print("REMOVING ELEMENTS")
print("=" * 50)

# Removing elements
items = ["pen", "pencil", "eraser", "ruler", "pencil"]
print(f"Original: {items}")

# Using remove (removes first occurrence)
items.remove("pencil")
print(f"After remove('pencil'): {items}")

# Using pop (removes and returns element)
popped = items.pop()
print(f"Popped item: {popped}")
print(f"After pop: {items}")

# Using pop with index
popped = items.pop(1)
print(f"Popped item at index 1: {popped}")
print(f"After pop(1): {items}")

print("\n" + "=" * 50)
print("LIST METHODS")
print("=" * 50)

# Various list methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# Sorting
numbers.sort()
print(f"Sorted: {numbers}")

# Reversing
numbers.reverse()
print(f"Reversed: {numbers}")

# Sorting in descending order
numbers.sort(reverse=True)
print(f"Sorted (descending): {numbers}")

print("\n" + "=" * 50)
print("LIST COMPREHENSION")
print("=" * 50)

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

print("\n" + "=" * 50)
print("COPYING LISTS")
print("=" * 50)

# Copying lists
original = [1, 2, 3]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print(f"Original: {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")
print(f"Copy 3: {copy3}")

print("\n" + "=" * 50)
print("JOINING LISTS")
print("=" * 50)

# Joining lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Combined: {combined}")
