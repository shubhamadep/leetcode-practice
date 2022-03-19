'''
[1,100,1,1,1,100,1,1,100,1]
[0,]

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        dp = [0] * (len(cost)+1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        
        return dp[-1]