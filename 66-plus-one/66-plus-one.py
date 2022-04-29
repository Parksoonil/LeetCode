class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        nums = 0
        for i in digits:
            nums = nums * 10 + i
            
        return [int(i) for i in str(nums + 1)]