import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        c = Counter(words)
        m = len(words)
        n = len(words[0])
        result = []
        for k in range(n):
            left = k
            subd = defaultdict(int)
            count = 0
            for j in range(k, len(s) - n + 1, n):
                word = s[j : j + n]
                if word in c:
                    subd[word] += 1
                    count += 1
                    while subd[word] > c[word]:
                        subd[s[left : left + n]] -= 1
                        left += n
                        count -= 1
                    if count == m:
                        result.append(left)
                else:
                    count = 0
                    left = j + n
                    subd = defaultdict(int)
        return result
        