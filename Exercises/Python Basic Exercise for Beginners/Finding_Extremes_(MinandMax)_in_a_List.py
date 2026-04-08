nums = [45, 2, 89, 12, 7]

print(f"largest: {max(nums)} smallest: {min(nums)}")

max_num = nums[0]
min_num = nums[0]

for i in nums:
    if max_num < i:
        max_num = i
    if(min_num > i):
        min_num = i
    else:
        continue
"""      
for i in nums:
    if min_num > i:
        min_num = i
        
    else:
        continue
"""
        
print(f"Largest: {max_num} Smallest: {min_num}")