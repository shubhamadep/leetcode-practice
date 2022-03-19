class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binary_search(num, end):
            left = 1
            right = end
            while left <= right:
                mid = left + (right - left) // 2
                if nums[lengths_at_index[mid]] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        lengths_at_index = [0] * (len(nums)+1)
        max_length = 0
        
        for i, num in enumerate(nums):
            new_length = binary_search(num, max_length)
            lengths_at_index[new_length] = i
            max_length = max(max_length, new_length)
        
        return max_length