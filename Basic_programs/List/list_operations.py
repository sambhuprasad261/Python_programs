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

lst2[1] = 200
print(lst2)

lst2.append(600)
print(lst2)

lst2.insert(2, 300)
print(lst2)

lst2.pop()
print(lst2)

lst2.pop(0)
print(lst2)

n = len(lst)
s = sum(lst)
print(s)
print(s/n)

lst3 = [100, 200, 300, 400, 500]
temp_lst = [0] * (len(lst3))
for i in range(len(lst3)):
    temp_lst[i] += lst3[len(lst3) - i - 1]
    
print(temp_lst)

print(temp_lst[::-1])

lst3.reverse()

print(lst3)


lst4 = [1, 2, 3, 4, 5, 6, 7]

temp2_lst = [x*x for x in lst4]

print(temp2_lst)

temp3_lst = []

for i in lst4:
    temp3_lst.append(i * i)
    
print(temp3_lst)