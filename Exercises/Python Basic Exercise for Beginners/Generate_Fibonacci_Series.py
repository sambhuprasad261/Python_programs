num = int(input("num = "))

add = 0
temp = 0
temp2 = 1
print(temp, temp2, end = " ")
for i in range(num - 2):
    add = temp + temp2
    print(f"{add}", end = " ")
    temp = temp2
    temp2 = add
    
    