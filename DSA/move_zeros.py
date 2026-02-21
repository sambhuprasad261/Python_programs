nums = [4,2,4,0,0,3,0,5,1,0]
i = j = 0
while j < len(nums):
    if nums[j] == 0:
        j += 1
    else:
        nums[i] = nums[j]
        i += 1
        j += 1
    for key in range(i, len(nums)):
        nums[key] = 0
    
print(nums)

"""
        
        i = 0

        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        nums[i:] = [0] * (len(nums) - i)
        """
        #method 1
        """
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                """
        """
        i = j = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        for key in range(i, len(nums)):
            nums[key] = 0

            """