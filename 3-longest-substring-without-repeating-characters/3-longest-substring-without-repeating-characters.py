class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = collections.defaultdict(int)
        i, j = 0, 0
        size = len(s)
        ans = 0
        
        while j < size:

            seen[s[j]] += 1            
            if len(seen) == j - i + 1:
                ans = max(ans, j - i + 1)
                j += 1
                
            elif len(seen) < j - i + 1:
                while len(seen) < j - i + 1:
                    seen[s[i]] -= 1
                    if seen[s[i]] == 0:
                        del seen[s[i]]
                    i += 1
                j += 1
        
        return ans
                
            