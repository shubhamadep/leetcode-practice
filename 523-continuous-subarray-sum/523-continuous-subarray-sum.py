'''
[24,2,4,6,7], k = 6
[23,25,29,35,42]
[5,1,5,5,0]

'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = collections.defaultdict(lambda: float('inf'))
        
        cs = 0
        for i in range(len(nums)):
            num = nums[i]
            cs += num
            target = cs % k
            
            if i > 0 and target == 0 or seen[target] < i - 1:
                return True
            
            seen[target] = min(i, seen[target])
        
        return False