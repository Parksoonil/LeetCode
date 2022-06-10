class Solution:
    def isHappy(self, n: int) -> bool:
        x = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in x:
                return False
            else:
                x.add(n)
        else:
            return True