class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                x += 1
            else:
                nums[i - x] = nums[i]
        return len(nums) - x
            