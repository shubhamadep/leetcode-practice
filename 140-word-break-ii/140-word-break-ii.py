class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        cache = {}
        wordDict = set(wordDict)
        
        def helper(idx):
            if idx == len(s):
                return [[]]
            
            if idx in cache:
                return cache[idx]
            
            can_reach = []
            for i in range(idx, len(s)):
                word = s[idx:i+1]
                if word in wordDict:
                    valid_sentences = helper(i+1)
                    for sentence in valid_sentences:
                        new_sentence = [word] + sentence
                        can_reach.append(new_sentence)
            
            cache[idx] = can_reach
            return cache[idx]
        
        word_breaks = helper(0)
        return [" ".join(sentence) for sentence in word_breaks]
                    