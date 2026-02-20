arr = [5, 4, 3, 2, 1]

print("Before Sorting arr = ", end = "")
print(arr)

for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if(arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("After Sorting arr = ", end = "")
print(arr)