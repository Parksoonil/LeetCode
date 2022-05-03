class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            m -= n[c] > 0
            n[c] -= 1
            if not m:
                while i < j and n[s[i]] < 0:
                    n[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]