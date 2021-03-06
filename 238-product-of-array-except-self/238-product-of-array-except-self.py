class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        result = []
        for i in range(n):
            result.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * p
            p = p * nums[i]
        return result