class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def helper(i, j):
            if j == -1 or i == -1:
                return 0
            
            val = 0
            if text1[i] == text2[j]:
                return helper(i-1, j-1) + 1
            else:
                return max(val, helper(i-1, j), helper(i, j-1))
            
        return helper(len(text1)-1, len(text2)-1)
        