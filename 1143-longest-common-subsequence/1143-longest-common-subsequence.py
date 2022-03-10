'''
  0abcde
0 000000
a 011
c 0
e 0


'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                
                if text1[row-1] == text2[col-1]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]
        
        
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         @cache
#         def helper(i, j):
#             if j == -1 or i == -1:
#                 return 0
            
#             val = 0
#             if text1[i] == text2[j]:
#                 return helper(i-1, j-1) + 1
#             else:
#                 return max(val, helper(i-1, j), helper(i, j-1))
            
#         return helper(len(text1)-1, len(text2)-1)
        