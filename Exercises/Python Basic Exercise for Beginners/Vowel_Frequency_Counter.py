sentence = input("sentence = ")
count = 0 
a_count = 0
vowel = "aeiou"

for i in sentence:
    if i in ["a", "e", "i", "o", "u"]:
        count = count + 1
    else:
        continue

print(count)


for i in sentence.lower():
    if i in vowel:
        a_count = a_count + 1
    else:
        continue
        
print(f"count is {a_count}")