# picture for solution explanation: https://leetcode.com/problems/diagonal-traverse-ii/discuss/597741/Clean-Simple-Easiest-Explanation-with-a-picture-and-code-with-comments

from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if not nums:
            return []
        
        result = []
        
        row = len(nums)
        hashset = set()
        hashmap = defaultdict(list)
        
        for i in range(row):
            col = len(nums[i])
            for j in range(col):
                hashmap[i+j].append(nums[i][j])
        
        for k in hashmap.keys():
            for value in reversed(hashmap[k]):
                result.append(value)
        
        return result