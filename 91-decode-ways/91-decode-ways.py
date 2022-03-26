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
        if s[0] == "0":
            return 0
    
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1: i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current
        
        return one_back