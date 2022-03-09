class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) < 3:
            return min(cost)
        
        def helper(idx, memo):
            if idx < 0:
                return 0
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = min(helper(idx-2, memo), helper(idx-1, memo)) + cost[idx]
            return memo[idx]
        
        return min(helper(len(cost)-1, {}), helper(len(cost)-2, {}))