class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        strlist = list(s)
        for i, v in enumerate(strlist):
            if v == "M":
                if i != 0 and strlist[i - 1] == "C":
                    result += 800
                else:
                    result += 1000
            elif v == "D":
                if i != 0 and strlist[i - 1] == "C":
                    result += 300
                else:
                    result += 500
            elif v == "C":
                if i != 0 and strlist[i - 1] == "X":
                    result += 80
                else:
                    result += 100
            elif v == "L":
                if i != 0 and strlist[i - 1] == "X":
                    result += 30
                else:
                    result += 50
            elif v == "X":
                if i != 0 and strlist[i - 1] == "I":
                    result += 8
                else:
                    result += 10
            elif v == "V":
                if i != 0 and strlist[i - 1] == "I":
                    result += 3
                else:
                    result += 5
            elif v == "I":
                result += 1
        return result
            