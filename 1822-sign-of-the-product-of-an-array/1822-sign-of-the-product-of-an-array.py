class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNegative = 0
        for num in nums:
            if num < 0:
                countNegative += 1
            elif num == 0:
                return 0
        return 1 if countNegative % 2 == 0 else - 1