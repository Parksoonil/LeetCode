class Solution:
    def reverse(self, x: int) -> int:
        s = (1 if x > 0 else -1)
        r = int(str(abs(x))[::-1])
        return (s*r if r < 2 ** 31 else 0)