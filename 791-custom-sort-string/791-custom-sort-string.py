class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts_s = collections.Counter(s)
        ans = ""
        
        for s in order:
            if s in counts_s:
                ans += s*counts_s[s]
                del counts_s[s]
        
        for char in counts_s.keys():
            ans += char*counts_s[char]
        
        return ans
        