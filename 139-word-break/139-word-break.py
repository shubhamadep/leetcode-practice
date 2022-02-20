class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        memo = {}
        
        def helper(word):
            if not word:
                return True
            
            if word in memo:
                return memo[word]
            
            for i in range(1, len(word)+1):
                word_ = word[:i]
                if word_ in wordDict:
                    val = helper(word[i:])
                    memo[word] = val
                    
                    if val:
                        return True
            
            return False
        
        return helper(s)
                    