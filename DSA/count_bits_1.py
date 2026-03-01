n = int(input("Enter Number: "))
s = ""
lst = []
count = 0

"""
while n > 0:
    
    s = s + str(n % 2)
    
    n = n // 2;
    
s = s[::-1]
    
for i in s:
    if int(i) == 1:
        count += 1
        
print(s)
lst.append(count)
    
print(lst)

"""


while n > 0:
    
    count = count + (n % 2 == 1)
    
    n = n // 2;
    
print(count)