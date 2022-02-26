class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dictionary = {}
        result = set([])
        
        if not nums:
            return []
        
        nums.sort()
        for left in range(len(nums) - 2):
            middle = left + 1
            right = len(nums) - 1
            
            while middle < right:
                tempSum = nums[left] + nums[middle] + nums[right] 
                if tempSum > 0:
                    right -= 1
                elif tempSum < 0:
                    middle += 1
                else:
                    result.add((nums[left], nums[middle], nums[right]))
                    right -= 1

        return result