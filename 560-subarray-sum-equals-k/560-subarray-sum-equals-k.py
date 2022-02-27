class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        cs = 0
        seen[0] = 1
        ans = 0
        
        for num in nums:
            cs += num
            if cs - k in seen:
                ans += seen[cs-k]
            seen[cs] += 1
        
        return ans