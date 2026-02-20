def majorityElement(nums):
    count = 0
    candidate = 0
    for i in nums:
        if count == 0:
            candidate = i
            count += 1
        else:
            if(candidate == i):
                count += 1
            else:
                count -= 1
    return candidate
print(majorityElement([1, 5, 7, 3, 4, 3, 8]))
