class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lengths = [1]* len(nums)
        
        for i in range(1, len(nums)):
            num1 = nums[i]
            for j in range(i):
                num2 = nums[j]
                
                if num2 < num1:
                    if lengths[i] < lengths[j] + 1:
                        lengths[i] = lengths[j] + 1
        
        return max(lengths)