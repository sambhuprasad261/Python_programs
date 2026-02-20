def invstar(num):
    for i in range(num, 0, -1):
        print("* "*i)
        
x = int(input("Choose any number that you wanted to print stars in inverted right angle format:"))

invstar(x)