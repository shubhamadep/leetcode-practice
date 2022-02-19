'''

[1,2,3,1,2] k=5

cs += curr_num
if cs - k in seen:
    ans += seen[cs-k]

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        seen[0] = 1
        cs = 0
        ans = 0
        for num in nums:
            cs += num
            if cs - k in seen:
                ans += seen[cs - k]
            seen[cs] += 1
        return ans