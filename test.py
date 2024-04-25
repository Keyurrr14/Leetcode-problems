nums = [5,8,96,0,8,3,0,8,0]
for i in range(len(nums)):
    if 0 in nums:
        nums.remove(0)
print(nums)