class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        asc, dsc = True, True
        
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            asc = False
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                continue
            dsc = False
        
        return asc or dsc
           
            
            
        