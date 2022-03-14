#https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/discuss/1537083/python-3-solution-hashmap-%2B-dynamic-programming
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = collections.defaultdict(int)
        max_length = 0
        for idx, num in enumerate(arr):
            seen[num] = seen[num-difference]+1
            max_length = max(max_length, seen[num])
        return max_length