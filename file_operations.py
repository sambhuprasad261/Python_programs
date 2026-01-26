"""
File Operations in Python
------------------------
Learn how to read from and write to files.
"""

import os

print("=" * 50)
print("WRITING TO A FILE")
print("=" * 50)

# Writing to a file (creates new file or overwrites existing)
filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    file.write("Python file operations are easy!\n")

print(f"Created and wrote to '{filename}'")

print("\n" + "=" * 50)
print("READING FROM A FILE")
print("=" * 50)

# Reading entire file
with open(filename, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print("\n" + "=" * 50)
print("READING LINE BY LINE")
print("=" * 50)

# Reading file line by line
with open(filename, "r") as file:
    print("Reading line by line:")
    for line_num, line in enumerate(file, 1):
        print(f"Line {line_num}: {line.strip()}")

print("\n" + "=" * 50)
print("READING ALL LINES INTO A LIST")
print("=" * 50)

# Reading all lines into a list
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    print(f"Lines: {lines}")

print("\n" + "=" * 50)
print("APPENDING TO A FILE")
print("=" * 50)

# Appending to a file (adds to end without overwriting)
with open(filename, "a") as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")

print(f"Appended to '{filename}'")

# Reading the updated file
with open(filename, "r") as file:
    print("\nUpdated content:")
    print(file.read())

print("\n" + "=" * 50)
print("WRITING MULTIPLE LINES")
print("=" * 50)

# Writing multiple lines at once
lines_to_write = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

multi_line_file = "multiline.txt"
with open(multi_line_file, "w") as file:
    file.writelines(lines_to_write)

print(f"Created '{multi_line_file}' with multiple lines")

# Reading it back
with open(multi_line_file, "r") as file:
    print("Content:")
    print(file.read())

print("\n" + "=" * 50)
print("FILE EXISTENCE CHECK")
print("=" * 50)

# Checking if file exists
if os.path.exists(filename):
    print(f"'{filename}' exists")
else:
    print(f"'{filename}' does not exist")

print("\n" + "=" * 50)
print("GETTING FILE INFORMATION")
print("=" * 50)

# Getting file information
if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"File: {filename}")
    print(f"Size: {file_size} bytes")
    print(f"Is file: {os.path.isfile(filename)}")
    print(f"Absolute path: {os.path.abspath(filename)}")

print("\n" + "=" * 50)
print("CLEANING UP")
print("=" * 50)

# Removing created files
try:
    os.remove(filename)
    print(f"Removed '{filename}'")
except FileNotFoundError:
    print(f"'{filename}' not found")

try:
    os.remove(multi_line_file)
    print(f"Removed '{multi_line_file}'")
except FileNotFoundError:
    print(f"'{multi_line_file}' not found")

print("\n" + "=" * 50)
print("FILE OPERATIONS WITH ERROR HANDLING")
print("=" * 50)

# Reading with error handling
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: Permission denied!")
except Exception as e:
    print(f"Error: {e}")

print("\nFile operations demonstration completed!")
