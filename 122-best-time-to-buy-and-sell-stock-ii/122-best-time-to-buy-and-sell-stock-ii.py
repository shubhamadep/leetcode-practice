class Solution:        
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i, holding):
            # Base case
            if i == len(prices): 
                return 0
            
            do_nothing = dp(i + 1, holding)
            do_something = 0

            if holding:
                # Sell stock
                do_something = prices[i] + dp(i + 1, 0)
            else:
                # Buy stock
                do_something = -prices[i] + dp(i + 1, 1)

            # Recurrence relation
            return max(do_nothing, do_something)

        return dp(0, 0)