class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result =[]
        for i in sorted(intervals, key = lambda i: i[0]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], i[1])
            else:
                result += i,
        return result
            