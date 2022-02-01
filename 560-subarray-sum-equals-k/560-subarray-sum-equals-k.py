class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        result = 0
        cs = 0
        seen[0] = 1
        
        for i in range(len(nums)):
            num = nums[i]
            cs += num
            if cs - k in seen:
                result += seen[cs-k]
            seen[cs] += 1
        
        return result
                