class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = map(int, version1.split('.')), map(int, version2.split('.'))
        v1, v2 = zip(*zip_longest(v1, v2, fillvalue = 0))
        return (0, 1, -1)[(v1 > v2) - (v1 < v2)]