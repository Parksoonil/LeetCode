class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        l = len(nums)
        while target >= nums[i]:
            if target == nums[i]:
                return i
            i += 1
            if i == l:
                return i
        return i
            