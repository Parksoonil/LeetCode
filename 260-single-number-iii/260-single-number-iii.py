class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for num in nums:
            tmp ^= num
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]