class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for colour in nums:
            counts[colour] += 1
        
        red, white, blue = counts
        nums[:red] = [0] * red
        nums[red: red + white] = [1] * white
        nums[red + white:] = [2] * blue