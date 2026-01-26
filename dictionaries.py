"""
Dictionaries in Python
---------------------
Learn about dictionary operations, methods, and manipulations.
"""

print("=" * 50)
print("CREATING DICTIONARIES")
print("=" * 50)

# Creating dictionaries
person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

print(f"Person: {person}")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

print("\n" + "=" * 50)
print("ACCESSING DICTIONARY VALUES")
print("=" * 50)

# Accessing values
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get method (safer - returns None if key doesn't exist)
print(f"City: {person.get('city')}")
print(f"Country: {person.get('country', 'Not specified')}")

print("\n" + "=" * 50)
print("MODIFYING DICTIONARIES")
print("=" * 50)

# Modifying values
student = {"name": "Alice", "grade": "B", "score": 85}
print(f"Original: {student}")

student["grade"] = "A"
print(f"After updating grade: {student}")

# Adding new key-value pairs
student["subject"] = "Math"
print(f"After adding subject: {student}")

print("\n" + "=" * 50)
print("REMOVING ITEMS")
print("=" * 50)

# Removing items
car = {"brand": "Toyota", "model": "Camry", "year": 2020, "color": "blue"}
print(f"Original: {car}")

# Using pop (removes and returns value)
color = car.pop("color")
print(f"Removed color: {color}")
print(f"After pop: {car}")

# Using del
del car["year"]
print(f"After del: {car}")

print("\n" + "=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

# Various dictionary methods
book = {
    "title": "Python Basics",
    "author": "Jane Smith",
    "pages": 300,
    "published": 2023
}

print(f"Book: {book}")
print(f"Keys: {list(book.keys())}")
print(f"Values: {list(book.values())}")
print(f"Items: {list(book.items())}")

print("\n" + "=" * 50)
print("ITERATING THROUGH DICTIONARIES")
print("=" * 50)

# Iterating through keys
print("Keys:")
for key in book.keys():
    print(f"  {key}")

# Iterating through values
print("\nValues:")
for value in book.values():
    print(f"  {value}")

# Iterating through key-value pairs
print("\nKey-Value pairs:")
for key, value in book.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("CHECKING IF KEY EXISTS")
print("=" * 50)

# Checking if key exists
if "author" in book:
    print("Author is present in the dictionary")

if "publisher" not in book:
    print("Publisher is not in the dictionary")

print("\n" + "=" * 50)
print("NESTED DICTIONARIES")
print("=" * 50)

# Nested dictionaries
school = {
    "student1": {
        "name": "Tom",
        "age": 15,
        "grade": "A"
    },
    "student2": {
        "name": "Emma",
        "age": 16,
        "grade": "B"
    }
}

print(f"School: {school}")
print(f"Student 1 name: {school['student1']['name']}")
print(f"Student 2 grade: {school['student2']['grade']}")

print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION")
print("=" * 50)

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

print("\n" + "=" * 50)
print("COPYING DICTIONARIES")
print("=" * 50)

# Copying dictionaries
original = {"a": 1, "b": 2, "c": 3}
copy1 = original.copy()
copy2 = dict(original)

print(f"Original: {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")

print("\n" + "=" * 50)
print("MERGING DICTIONARIES")
print("=" * 50)

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update method
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"Merged using update: {dict1_copy}")

# Using unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print(f"Merged using unpacking: {merged}")
