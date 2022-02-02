class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        R, C = len(points), len(points[0])
        dp = [points[0][x] for x in range(len(points[0]))]
        
        for row in range(1, len(points)):
            leftMax = dp
            rightMax = dp
            
            for col in range(1, C):
                leftMax[col] = max(leftMax[col-1]-1, dp[col])
            
            for col in range(C-2, -1, -1):
                rightMax[col] = max(rightMax[col+1]-1, dp[col])
            
            for i in range(len(dp)):
                dp[i] = points[row][i] + max(leftMax[i], rightMax[i])
        
        return max(dp)