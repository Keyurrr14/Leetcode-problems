class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.Search(nums, target, True)
        right = self.Search(nums, target, False)
        return [left, right]

    def Search(self, nums, target, leftMost):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    i = mid
                    if leftMost:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i