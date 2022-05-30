class Solution:
    def rob(self, nums: List[int]) -> int:
        max_3_house, max_2_house, adj = 0, 0, 0
        
        for cur in nums:
            max_3_house, max_2_house, adj = max_2_house, adj, max(max_3_house + cur, max_2_house + cur)
        
        return max(max_2_house, adj)