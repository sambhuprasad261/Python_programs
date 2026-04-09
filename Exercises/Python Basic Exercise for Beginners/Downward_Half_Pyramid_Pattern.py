num = int(input("Enter rows: "))

for i in range(num, -1, -1):
    for j in range(i):
        print("*", end = " ")
    print()