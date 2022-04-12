class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        state, value, sign = 0, 0, 1
        for char in s:
            if state == 0:
                if char == " ":
                    state = 0
                elif char == "+" or char ==  "-":
                    sign = 1 if char == "+" else -1
                    state = 1
                elif char.isdigit():
                    value = value * 10 + int(char)
                    state = 2
                else:
                    return 0
            elif state == 1:
                if char.isdigit():
                    value = value * 10 + int(char)
                    state = 2
                else:
                    return 0
            elif state == 2:
                if char.isdigit():
                    value = value * 10 + int(char)
                    state = 2
                else:
                    break
                
            
            
        value = sign * value
        value = max(-(2 ** 31), min(value, 2 ** 31 - 1))
        return value
            