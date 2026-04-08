str_x = "Emma is good developer. Emma is a writer"

lst = str_x.split(" ")
count = 0

for i in lst:
    if "Emma" in i:
        count = count + 1
    else:
        continue

print(count)

print(f"another method sub string count is {str_x.count("Emma")}")