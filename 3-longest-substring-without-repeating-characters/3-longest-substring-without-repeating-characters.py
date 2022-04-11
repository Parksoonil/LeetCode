class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        results = start = 0
        strs = {}
        for i, char in enumerate(s):
            if char in strs and start <= strs[char]:
                start = strs[char] + 1
            else:
                results = max(results, i - start + 1)
            strs[char] = i
        return results