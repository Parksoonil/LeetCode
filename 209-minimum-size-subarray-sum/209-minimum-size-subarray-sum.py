class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, result = 0, len(nums) + 1
        
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                result = min(result, j - i + 1)
                target += nums[i]
                i += 1
        return result % (len(nums) + 1)