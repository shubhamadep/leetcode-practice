'''

# Method 1 : Kadane's Algorithm
        if max(A) <= 0:
            return max(A)
        
        max_sum = curr_max = min_sum = curr_min = A[0] 
        
        for i in range(1, len(A)): 
            curr_max = max(A[i], curr_max + A[i]) 
            max_sum = max(max_sum, curr_max)
            curr_min = min(A[i], curr_min + A[i]) 
            min_sum = min(min_sum, curr_min)
            
        return max(max_sum, sum(A) - min_sum)

1,-2,3,-2,1,-2,3

'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        
        max_sum = float('-inf')
        min_sum = float('inf')
        max_cs = 0
        min_cs = 0
        
        for num in nums:
            max_cs = max(num, max_cs+num)
            min_cs = min(num, min_cs+num)
            max_sum = max(max_sum, max_cs)
            min_sum = min(min_sum, min_cs)
        
        return max(max_sum, sum(nums)-min_sum)