class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        def helper(i, j, remaining):
            if remaining == -1:
                return False
            if j-i+1 <= 1:  # if length is <= 1
                return True
            if (i, j, remaining) in memo:
                return memo[(i, j, remaining)]
            
            if s[i] == s[j]:
                memo[(i, j, remaining)] = helper(i+1, j-1, remaining)
            else:
                memo[(i, j, remaining)] = helper(i+1, j, remaining-1) or helper(i, j-1, remaining-1)
            return memo[(i, j, remaining)]
        
        memo = {}
        return helper(0, len(s)-1, k)