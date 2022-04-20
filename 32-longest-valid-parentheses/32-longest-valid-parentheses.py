class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [(-1, ')')], 0
        for i, v in enumerate(s):
            if v == ')' and stack [-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, v),
        return result