class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countofS = collections.Counter(s)
        ans = []
        
        for c in order:
            ans.append(countofS[c] * c)
            countofS[c] = 0
        
        for char in countofS:
            ans.append(countofS[char] * char)
        
        return "".join(ans)