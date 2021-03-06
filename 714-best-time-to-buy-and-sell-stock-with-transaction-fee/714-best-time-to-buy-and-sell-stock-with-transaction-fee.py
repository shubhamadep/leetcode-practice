class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        max_profit = 0
        hold = - prices[0]
        
        for i in range(1, len(prices)):
            price = prices[i]
            max_profit = max(max_profit, hold+price-fee)
            hold = max(hold, max_profit - price)
        
        return max_profit
    
#     def maxProfit(self, prices: List[int], fee: int) -> int:
        
#         # 0 - not holding, 1 - holding
#         def dp(idx, holding):
#             if idx == len(prices):
#                 return 0
            
#             if (idx, holding) in memo:
#                 return memo[(idx, holding)]
            
#             do_nothing = dp(idx+1, holding)
            
#             do_something = 0
#             if holding:
#                 do_something = prices[idx] + dp(idx+1, 0) - fee
#             else:
#                 do_something = - prices[idx] + dp(idx+1, 1)
            
#             memo[(idx, holding)] = max(do_nothing, do_something)
#             return memo[(idx, holding)]
        
#         memo = {}
#         return dp(0, 0)