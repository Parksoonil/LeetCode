class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        tmp = 0
        
        a = list(a)
        b = list(b)
        while a or b or tmp:
            if a:
                tmp += int(a.pop())
            if b:
                tmp += int(b.pop())
            
            result += str(tmp % 2)
            
            tmp //= 2
        return result[::-1]