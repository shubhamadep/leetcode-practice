class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1 for i in range(len(nums))]
        n = len(nums)
        
        for i in reversed(range(2*len(nums))):
            while stack and nums[i%n] >= nums[stack[-1]]:
                stack.pop()
            result[i%n] = nums[stack[-1]] if stack else -1
            stack.append(i%n)
        
        return result