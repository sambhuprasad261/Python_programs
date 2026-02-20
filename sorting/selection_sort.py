arr = [10, 3, 5, 2, 7, 4, 20, 17]
n = len(arr)

print("The Unsorted arr = ", end = "")
print(arr)

for i in range(n - 1):
    val = i
    for j in range(i + 1, n):
        if(arr[j] < arr[val]):
            val = j
    arr[i], arr[val] = arr[val], arr[i];
    
print("The Sorted arr = ", end = "")
print(arr)