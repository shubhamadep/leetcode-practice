class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_select(start, end, k):

            while True:
                
                left = start + 1
                right = end
                pivot = start
                
                while left <= right:
                    left_num, pivot_num, right_num = nums[left], nums[pivot], nums[right]
                    
                    if pivot_num < left_num and pivot_num > right_num:
                        nums[left], nums[right] = nums[right], nums[left]
                    
                    elif pivot_num <= right_num:
                        right -= 1
                    
                    elif pivot_num >= left_num:
                        left += 1
                
                nums[pivot], nums[right] = nums[right], nums[pivot]
                
                if right == k:
                    return nums[right]
                
                if k > right:
                    start = right + 1
                
                else:
                    end = right - 1
            
            return -1
        
        if k > len(nums):
            return -1
        
        return quick_select(0, len(nums)-1, len(nums)-k)