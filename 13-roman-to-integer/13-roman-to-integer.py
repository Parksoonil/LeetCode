class Solution:
    def romanToInt(self, s: str) -> int:
        result, prev = 0, 0
        dict = { "I":1, "V":5, "X":10, "L":50,
                 "C":100, "D":500, "M":1000}
        for i in s[::-1]:
            if dict[i] >= prev:
                result += dict[i]
            else:
                result -= dict[i]
            prev = dict[i]
        return result