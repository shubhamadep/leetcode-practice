class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        max_window = 0
        
        i, j = 0, 0
        count = 0
        while j < len(nums):
            num = nums[j]
            if num == 0:
                count += 1
            
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1
            max_window = max(max_window, j - i + 1)
            j += 1
        
        return max_window