class Solution:
    def minCut(self, string: str) -> int:
    
        dp = [ [False for sj in string] for si in string ]
        for i in range(len(string)):
            dp[i][i] = True
        for length in range(2, len(dp) + 1):
            for i in range(0, len(string) - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = string[i] == string[j]
                else:
                    dp[i][j] = ( string[i] == string[j]) and dp[i+1][j-1]

        cuts = [float("inf") for _ in string]
        for i in range(len(string)):
            if dp[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = cuts[i-1] + 1
                for j in range(1, i):
                    if dp[j][i] and cuts[j - 1] + 1 < cuts[i]:
                        cuts[i] = cuts[j-1] + 1

        return cuts[-1]