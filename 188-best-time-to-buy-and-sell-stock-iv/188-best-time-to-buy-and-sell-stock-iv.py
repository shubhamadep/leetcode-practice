'''

[3,2,6,5,0,3] k = 2

for k = 1 
[0,0,4,4,4,4]

for k = 2
[0,0,4,4,4,0]

sell at 4 and buy at 4 and sell at 5
4 - 0 + 3 = 7
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(idx, transactions_remaining, holding):
            if idx == len(prices) or transactions_remaining == 0:
                return 0
            
            do_nothing = dp(idx+1, transactions_remaining, holding)
            do_something = 0
            
            if holding:
                do_something = prices[idx] + dp(idx+1, transactions_remaining-1, 0)
            else:
                do_something = - prices[idx] + dp(idx+1, transactions_remaining, 1)
            
            return max(do_something, do_nothing)
        
        return dp(0, k, 0)