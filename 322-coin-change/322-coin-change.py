'''

coins = [1, 2, 5]
capacity / amount = 11

choices : take 1 or dont take 1
if take 1: find -> minimum number of coins required to make amount - 1 ; else amount

dp = [0, 1, 2, 3, 4]

minimumNumberOfCoins(n) = min( minimumNumberOfCoins(n-x), minimumNumberOfCoins(n-y),                                              minimumNumberOfCoins(n-z))
memoization = []
                    
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, len(dp)):
            for coin in coins:
                if i - coin > 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1