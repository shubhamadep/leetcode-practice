class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i, j, k = 0, len(nums)-1, len(nums)-1
        
        while i <= j:
            l_num = nums[i]
            r_num = nums[j]
            if abs(l_num) > abs(r_num):
                result[k] = l_num * l_num
                i += 1
            else:
                result[k] = r_num * r_num
                j -= 1
            k -= 1
        
        return result