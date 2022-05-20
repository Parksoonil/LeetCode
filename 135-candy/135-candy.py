class Solution:
    def candy(self, ratings: List[int]) -> int:
        result = len(ratings) * [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                result[i - 1] = max(result[i - 1], result[i] + 1)
        return sum(result)