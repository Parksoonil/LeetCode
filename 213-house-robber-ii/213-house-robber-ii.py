class Solution:
    def rob(self, nums: List[int]) -> int:
        def linearRob(i, j):
            rob1 = rob2 = 0
            for k in range(i, j):
                rob1, rob2 = rob2 + nums[k], max(rob1, rob2)
            return max(rob1, rob2)
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            return max(linearRob(0, n - 1), linearRob(1, n))