class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        left, right = 0, len(nums)-1
        missing = lambda idx: nums[idx] - nums[0] - idx
        
        while left <= right:
            
            mid = left + ( right - left ) // 2
            
            if missing(mid) < k:
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[right] + k - missing(right)