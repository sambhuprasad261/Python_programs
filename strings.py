"""
String Operations in Python
--------------------------
Learn about string manipulation and methods.
"""

print("=" * 50)
print("CREATING STRINGS")
print("=" * 50)

# Different ways to create strings
single_quote = 'Hello'
double_quote = "World"
multi_line = """This is a
multi-line
string"""

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Multi-line:\n{multi_line}")

print("\n" + "=" * 50)
print("STRING CONCATENATION")
print("=" * 50)

# Concatenating strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Using join
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(f"Sentence: {sentence}")

print("\n" + "=" * 50)
print("STRING FORMATTING")
print("=" * 50)

# Different formatting methods
name = "Alice"
age = 25

# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# format method
print("My name is {} and I am {} years old.".format(name, age))

# % formatting (old style)
print("My name is %s and I am %d years old." % (name, age))

print("\n" + "=" * 50)
print("STRING METHODS - CASE CONVERSION")
print("=" * 50)

# Case conversion
text = "Python Programming"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Swap case: {text.swapcase()}")

print("\n" + "=" * 50)
print("STRING METHODS - CHECKING")
print("=" * 50)

# Checking string properties
text1 = "Hello123"
text2 = "Hello"
text3 = "123"

print(f"'{text1}' is alphanumeric: {text1.isalnum()}")
print(f"'{text2}' is alphabetic: {text2.isalpha()}")
print(f"'{text3}' is digit: {text3.isdigit()}")
print(f"'{text2}' is lowercase: {text2.islower()}")
print(f"'{text2}' is uppercase: {text2.isupper()}")

print("\n" + "=" * 50)
print("STRING METHODS - SEARCHING")
print("=" * 50)

# Searching in strings
sentence = "Python is easy to learn and Python is powerful"

print(f"Sentence: {sentence}")
print(f"Count 'Python': {sentence.count('Python')}")
print(f"Find 'easy': {sentence.find('easy')}")
print(f"Index of 'learn': {sentence.index('learn')}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'powerful': {sentence.endswith('powerful')}")

print("\n" + "=" * 50)
print("STRING METHODS - REPLACING")
print("=" * 50)

# Replacing substrings
text = "I like apples and apples are healthy"
print(f"Original: {text}")
print(f"Replace 'apples' with 'oranges': {text.replace('apples', 'oranges')}")
print(f"Replace first 'apples': {text.replace('apples', 'oranges', 1)}")

print("\n" + "=" * 50)
print("STRING METHODS - SPLITTING AND JOINING")
print("=" * 50)

# Splitting strings
sentence = "Python,Java,JavaScript,Ruby"
languages = sentence.split(",")
print(f"Original: {sentence}")
print(f"Split by comma: {languages}")

# Splitting by whitespace
text = "Hello World Python"
words = text.split()
print(f"Split by whitespace: {words}")

# Joining strings
joined = "-".join(languages)
print(f"Joined with '-': {joined}")

print("\n" + "=" * 50)
print("STRING METHODS - STRIPPING")
print("=" * 50)

# Removing whitespace
text = "   Python   "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Left strip: '{text.lstrip()}'")
print(f"Right strip: '{text.rstrip()}'")

print("\n" + "=" * 50)
print("STRING SLICING")
print("=" * 50)

# Slicing strings
text = "Python Programming"
print(f"Original: {text}")
print(f"First 6 characters: {text[:6]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Characters 7-17: {text[7:18]}")
print(f"Every other character: {text[::2]}")
print(f"Reversed: {text[::-1]}")

print("\n" + "=" * 50)
print("STRING LENGTH AND CHARACTER ACCESS")
print("=" * 50)

# Length and character access
word = "Python"
print(f"Word: {word}")
print(f"Length: {len(word)}")
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")

# Iterating through string
print("Characters:")
for char in word:
    print(f"  {char}")

print("\n" + "=" * 50)
print("STRING ALIGNMENT")
print("=" * 50)

# Aligning strings
text = "Python"
print(f"Center (20): '{text.center(20)}'")
print(f"Left align (20): '{text.ljust(20)}'")
print(f"Right align (20): '{text.rjust(20)}'")
print(f"Zero fill (10): '{text.zfill(10)}'")
