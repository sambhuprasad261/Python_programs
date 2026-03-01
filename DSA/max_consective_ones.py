def findMaxConsecutiveOnes(nums: List[int]) -> int:
    c1 = 0
    lst = []
    for i in nums:
        if i != 1:
            lst.append(c1)
            c1 = 0

        else:
            c1 += 1
    lst.append(c1)

    return max(lst)
    
print(findMaxConsecutiveOnes([1, 1, 1, 0, 1, 1, 1, 1]))