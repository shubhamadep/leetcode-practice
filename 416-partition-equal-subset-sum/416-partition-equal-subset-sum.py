'''

num choices:

1. can take in first - helper(idx+1, subset_sum + num) 
2. can take in second - helper(idx, subset_sum) 

if subset_sum == total_sum // 2:
    return True

'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        self.memo = {}
        def helper(idx, subset_sum):
            if idx == 0:
                if subset_sum == 0:
                    return True
                return False
            
            if (idx, subset_sum) in self.memo:
                return self.memo[(idx, subset_sum)]
            
            if subset_sum == 0:
                return True
            
            self.memo[(idx, subset_sum)] = helper(idx-1, subset_sum - nums[idx]) or helper(idx-1, subset_sum) 
            return self.memo[(idx, subset_sum)]
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        subset_sum = total_sum // 2
        
        return helper(len(nums)-1, subset_sum)
        