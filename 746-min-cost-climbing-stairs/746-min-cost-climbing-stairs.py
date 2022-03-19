'''
[1,100,1,1,1,100,1,1,100,1]
[0,]

'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        
        #dp = [0] * (len(cost)+1)
        prev_1 = 0
        prev_2 = 0
        
        for i in range(2, len(cost)+1):
            temp = min(prev_1+cost[i-2], prev_2+cost[i-1])
            prev_1 = prev_2
            prev_2 = temp
        
        return prev_2