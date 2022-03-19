class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        prev_dp = [0]*(amount+1)
        prev_dp[0] = 1
        
        for coin in coins:
            new_dp = [0]*(amount+1)
            new_dp[0] = 1
            for amt in range(1, amount+1):
                if amt >= coin:
                    new_dp[amt] += new_dp[amt-coin] + prev_dp[amt]
                else:
                    new_dp[amt] += prev_dp[amt]
                    
            prev_dp = new_dp
        
        return new_dp[-1]
    
#         for row in range(1, len(dp)):
#             for col in range(1, len(dp[0])):
#                 coin = coins[row-1]
#                 if col >= coin:
#                     dp[row][col] += dp[row][col-coin] + dp[row-1][col]
#                 else:
#                     dp[row][col] += dp[row-1][col]
        
#         return dp[-1][-1]
                
        
#         @functools.lru_cache(None)
#         def dp(amount: int, n: int) -> int:
#             if amount == 0:
#                 return 1
            
#             if n < 0 or amount < 0:
#                 return 0
            
#             return dp(amount - coins[n], n) + dp(amount, n-1)
        
#         return dp(amount, len(coins) - 1)

            
    
        