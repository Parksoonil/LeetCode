class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        def palin(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        if len(s) < 2 or s == s[::-1]:
            return s
        for i in range(len(s) - 1):
            result = max(result, palin(i, i + 1), palin(i, i + 2), key = len)
        return result
            