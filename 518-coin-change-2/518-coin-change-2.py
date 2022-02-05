class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                coin = coins[i-1]
                if coin <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coin]
                else:
                    dp[i][j] = dp[i-1][j]
        
        
        print(dp)
        return dp[len(coins)][amount]