class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def lcs(word1, word2):
            dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
            
            for i in range(1, len(dp)):
                for j in range(1, len(dp[0])):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[-1][-1]
        
        lcs = lcs(word1, word2)
        return len(word1) + len(word2) - 2*lcs