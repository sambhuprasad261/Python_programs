def merge(arr, left, mid, right):
    
    n1 = mid - left + 1
    n2 = right - mid
    
    l1 = []
    r1 = []
    
    for i in range(n1):
        
        l1.append(arr[left + i])
    
    for j in range(n2):
        
        r1.append(arr[mid + 1 + j])
        
    i = 0
    j = 0
    k = left
        
    while(i < n1 and j < n2):
        
        if(l1[i] <= r1[j]):
            
            arr[k] = l1[i]
            i += 1
            
        else:
            
            arr[k] = r1[j]
            j += 1
        
        k += 1
        
    while(i < n1):
        
        arr[k] = l1[i]
        i += 1
        k += 1
        
    while(j < n2):
        
        arr[k] = r1[j]
        j += 1
        k += 1
    

def merge_sort(arr, left, right):
    
    if(left < right):
        
        mid =  (right + left) // 2
        
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        merge(arr, left, mid, right)

lst = [10, 5, 25, 15, 35, 25, 30]

print("Before Sorting Array is: ", end = "")
print(lst)

merge_sort(lst, 0, len(lst) - 1)

print("After Sorting Array is: ", end = "")
print(lst)