# This is O(logn) solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def helper(left, right):
            if left == right:
                return left
            
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                return helper(left, mid)
            return helper(mid+1, right)
        
        
        return helper(0, len(nums)-1)