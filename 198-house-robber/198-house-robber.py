class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def helper(idx):
            if idx == 0:
                return nums[idx]
            if idx == 1:
                return max(nums[idx], nums[idx-1])
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = max(helper(idx-2)+nums[idx], helper(idx-1))
            return memo[idx]
        
        return helper(len(nums)-1)