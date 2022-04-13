class Solution:
    def intToRoman(self, num: int) -> str:
        strs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for i, v in enumerate(values):
            result += (num//v) * strs[i]
            num %= v
        return result
            