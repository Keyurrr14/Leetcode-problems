class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 2:
            return nums.reverse()

        pointer = len(nums)-2
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1

        if pointer == -1:
            return nums.reverse()

        for i in range(len(nums) - 1, pointer, -1):
            if nums[pointer] < nums[i]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                break

        nums[pointer + 1:] = reversed(nums[pointer + 1:])
        