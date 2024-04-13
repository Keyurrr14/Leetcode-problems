class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1

        return left
    
# Initialze the left and right to 1 because 0th index element is not gonna change
# right iterates through the entire nums list
# we compare the current right pointer to the previous one, and if they are not equal meaining they are unique, and put them in the position of the left pointer. Increment the left pointer
# return left as it indiactes the number of duplicates