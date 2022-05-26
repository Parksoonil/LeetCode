class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        prev_max = nums[0]
        prev_min = nums[0]
        max_n = nums[0]
        min_n = nums[0]
        result = nums[0]
        
        for i in nums[1:]:
            max_n = max(max(prev_max * i, prev_min * i), i)
            min_n = min(min(prev_max * i, prev_min * i), i)
            prev_max = max_n
            prev_min = min_n
            result = max(result, max_n)
        return result