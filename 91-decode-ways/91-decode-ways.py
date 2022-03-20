# class Solution:

#     @lru_cache(maxsize=None)
#     def recursiveWithMemo(self, index, s) -> int:
#         # If you reach the end of the string
#         # Return 1 for success.
#         if index == len(s):
#             return 1

#         # If the string starts with a zero, it can't be decoded
#         if s[index] == '0':
#             return 0

#         if index == len(s)-1:
#             return 1
        
#         answer = self.recursiveWithMemo(index + 1, s)
#         if int(s[index : index + 2]) <= 26:
#             answer += self.recursiveWithMemo(index + 2, s)

#         return answer

#     def numDecodings(self, s: str) -> int:
#         return self.recursiveWithMemo(0, s)

class Solution:
    def numDecodings(self, s: str) -> int:
        # Array to store the subproblem results
        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        dp[1] = 0 if s[0] == '0' else 1


        for i in range(2, len(dp)):

            # Check if successful single digit decode is possible.
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i - 2 : i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i - 2]
                
        return dp[len(s)]
            