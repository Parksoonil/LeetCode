class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isMinus = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            i, temp = 1, divisor
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        if isMinus:
            result = -result
        return min(max(-2147483648, result), 2147483647)
            