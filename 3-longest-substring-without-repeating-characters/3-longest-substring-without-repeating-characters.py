class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0
        
        st, end = 0, 0
        dictionary = {}
        ls = 0
        
        while end < len(s):
            if s[end] in dictionary and dictionary[s[end]] >= st:
                st = dictionary[s[end]] + 1
            dictionary[s[end]] = end
            ls = max(ls, end - st + 1)
            end += 1
        
        return ls
                
            