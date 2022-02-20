class Solution:
    def countSubstrings(self, s: str) -> int:
        
        dp = [[ 0 for _ in range(len(s))] for _ in range(len(s))]
        count = 0
        
        for i in range(len(s)):
            dp[i][i] = 1
            count += 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                dp[i-1][i] = 1
                count += 1

        for gap in range(2, len(s)):
            for i in range(len(s) - gap):
                j = i + gap
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    count += 1
                
        
        return count