class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = [[]]
        for _ in range(k):
            result = [[i] + c for c in result for i in range(1, c[0] if c else n + 1)]
        return result