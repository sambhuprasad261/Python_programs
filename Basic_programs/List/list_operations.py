lst = [10, 20, 30, 40, 50]

lst2 = []

print(lst[2])

count = 0
for i in lst:
    count += 1

print("Length of the list = ", count)

print("Length using in bulit is ", len(lst))

print(lst == [])

if(lst == []):
    print("List1 is Empty")
else:
    print("List1 is not Empty")

if(len(lst2) == 0):
    print("List2 is Empty")
else:
    print("List 2 is not Empty")
    

lst2 = [10, 20, 30, 40, 50]

lst[1] = 200
print(lst2)

lst2.append(600)
print(lst2)

lst2.insert(2, 300)
print(lst2)

lst2.pop()
print(lst2)

