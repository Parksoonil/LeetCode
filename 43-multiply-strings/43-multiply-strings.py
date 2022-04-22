class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if not n or not m:
            return '0'
        res = [0] * (n + m)
        for i in reversed(range(n)):
            carry = 0
            for j in reversed(range(m)):
                tmp = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0')) + carry
                carry = (res[i+j+1]+tmp) // 10
                res[i+j+1] = (res[i+j+1]+tmp) % 10
            res[i] += carry
        res = ''.join(map(str, res))
        return '0' if not res.lstrip('0') else res.lstrip('0')