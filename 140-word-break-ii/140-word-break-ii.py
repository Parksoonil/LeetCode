class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        result = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                result.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    result.append(item)
        
        memo[s] = result
        
        return result