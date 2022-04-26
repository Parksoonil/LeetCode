class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        numSum = result = nums[0]
        
        for i in range(1, len(nums)):
            numSum = max(nums[i], nums[i] + numSum)
            result = max(numSum, result)
        return result