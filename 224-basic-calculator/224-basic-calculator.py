class Solution:
    def calculate(self, s: str) -> int:
        result, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ['-', '+']:
                result += sign * num
                num = 0
                sign = [-1, 1][ss == "+"]
            elif ss == "(":
                stack.append(result)
                stack.append(sign)
                sign, result = 1, 0
            elif ss == ")":
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        return result + num * sign