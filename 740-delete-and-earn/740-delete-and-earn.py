class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         counts = collections.Counter(nums)
#         total_gain = collections.defaultdict(int)
#         for item in counts:
#             total_gain[item] = counts[item]*item
        
#         max_item = max(total_gain.keys())
        
#         def helper(item):
#             if item == 0:
#                 return 0
#             if item == 1:
#                 return total_gain[item]
            
#             return max(helper(item-2)+total_gain[item], helper(item-1))
        
#         return helper(max_item)
    
    
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        total_gain = collections.defaultdict(int)
        for item in counts:
            total_gain[item] = counts[item]*item
        
        max_item = max(total_gain.keys())
        
        dp = [0]*(max_item+1)
        dp[1] = total_gain[1]
        
        for item in range(2, len(dp)):
            dp[item] = max(dp[item-2]+total_gain[item], dp[item-1])
        
        return dp[-1]