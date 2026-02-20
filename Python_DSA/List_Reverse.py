def reverse(nums):
    l, r = 0, len(nums) -1
    
    while l < r:
        nums[l] = nums[l] ^ nums[r]
        nums[r] = nums[l] ^ nums[r]
        nums[l] = nums[l] ^ nums[r]
        #temp = nums[l]
        #nums[l] = nums[r]
        #nums[r] = temp
        l += 1
        r -= 1
    return nums
print(reverse([1, 2, 3, 4, 5]))