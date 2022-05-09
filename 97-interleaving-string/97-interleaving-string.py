class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)
        if x + y != z:
            return False
        dp = [[True for _ in range(y + 1)] for _ in range(x + 1)]
        for i in range(1, x + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, y + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, x + 1):
            for j in range(1, y + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or\
                    (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]