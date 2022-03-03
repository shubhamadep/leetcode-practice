class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        store_diagonal_elements = collections.defaultdict(list)
        result = []
        
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                store_diagonal_elements[row+col].append(nums[row][col])
            
        for idx in sorted(store_diagonal_elements.keys()):
            if idx in store_diagonal_elements:
                result += store_diagonal_elements[idx][::-1]
        
        return result
    
    
# from collections import defaultdict
# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         if not nums:
#             return []
        
#         result = []
        
#         row = len(nums)
#         hashset = set()
#         hashmap = defaultdict(list)
        
#         for i in range(row):
#             col = len(nums[i])
#             for j in range(col):
#                 hashmap[i+j].append(nums[i][j])
        
#         for k in hashmap.keys():
#             for value in reversed(hashmap[k]):
#                 result.append(value)
        
#         return result