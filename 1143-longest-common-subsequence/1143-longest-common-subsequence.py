class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if memo[p1][p2] != -1:
                return memo[p1][p2]
            
            # Recursive case 1.
            if text1[p1] == text2[p2]:
                memo[p1][p2] = 1 + memo_solve(p1 + 1, p2 + 1)
            
            # Recursive case 2.
            else:
                memo[p1][p2] =  max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
            return memo[p1][p2]
            
        return memo_solve(0, 0)