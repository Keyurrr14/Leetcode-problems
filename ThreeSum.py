class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, dig in enumerate(nums):
            if i>0 and dig == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = dig + nums[l] + nums[r]
                if sum>0:
                    r -= 1
                elif sum<0:
                    l += 1
                else:
                    res.append([dig, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        

        return res


# enumerate returns a tuple (index, character at that index)
# since items are sorted, we check if the current  number is same as previous one to avoid duplicates
# then we declare the left and right pointers
# we add them and 
# if sum>0 we decrement right pointer
# if sum<0 we increment left pointer
# if it equals to zero, then we append it in the result