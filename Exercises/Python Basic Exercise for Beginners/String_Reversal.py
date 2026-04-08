text = input("text = ")

def rev_txt(text):
    temp_txt = ""
    for i in range(len(text) - 1, -1, -1):
        temp_txt = temp_txt + text[i]
    return temp_txt
    
str_rev = rev_txt(text)
  
print("Reversed:", str_rev)

str_rev_a = text[::-1]

print("rev:", str_rev_a)