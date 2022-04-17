class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(idx, comb, k):
            if len(comb) == k:
                output.append(comb[:])
                return
            
            for i in range(idx, len(nums)):
                comb.append(nums[i])
                helper(i+1, comb, k)
                comb.pop()
        
        output = []
        for k in range(len(nums)+1):
            helper(0, [], k)
        
        return output