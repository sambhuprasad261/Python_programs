lst = [1, 2, 3, 4, 5, 6, 7]
target = 7
rst = []
n = len(lst)

for i in range(n):
    for j in range(1, n):
        #print("j = ", j)
        #print("i = ", i)
        if lst[i] + lst[j] == target:
            rst.append([lst[i], lst[j]])
   
print(rst)   