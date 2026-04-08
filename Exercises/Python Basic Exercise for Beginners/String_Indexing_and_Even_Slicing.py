
"""

Display only those characters which are present at an even index number in given string.

"""
"Another Method"

"""
s = input("Enter the string: ")

l = len(s)

print(f"Original String is {s}")

print("Printing only even index chars")

for i in range(l):
    if(i % 2 == 0):
        print(s[i])
    else:
        continue
        
        """

s = input("Enter the String: ")

E_slic = s[::2]

#print(E_slic)

for i in E_slic:
    print(i)