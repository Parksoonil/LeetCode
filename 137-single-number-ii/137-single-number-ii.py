class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        neg = False
        for i in range(32):
            counter = 0
            
            for num in nums:
                if (num >> i) & 1:
                    counter += 1
            
            if counter % 3 == 1:
                result += pow(2, i)
                if i == 31:
                    neg = True
        return result if not neg else result - pow(2, 32)