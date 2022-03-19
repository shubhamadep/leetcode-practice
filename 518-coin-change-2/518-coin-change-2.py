class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dp(amount: int, n: int) -> int:
            if amount == 0:
                return 1
            
            if n < 0 or amount < 0:
                return 0
            
            return dp(amount - coins[n], n) + dp(amount, n-1)
        
        return dp(amount, len(coins) - 1)