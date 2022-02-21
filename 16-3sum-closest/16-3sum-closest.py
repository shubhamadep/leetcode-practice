class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minimum_diff = float('inf')
        minimum_sum = float('inf')
        
        for i in range(len(nums)):
            num1 = nums[i]
            j = i + 1
            k = len(nums)-1
            while j < k:
                num2 = nums[j]
                num3 = nums[k]
                sum = num1 + num2 + num3

                if sum == target:
                    return target

                if abs(target - sum) < minimum_diff:
                    minimum_diff = abs(target - sum)
                    minimum_sum = sum

                if sum > target:
                    k -= 1
                else:
                    j += 1

        return minimum_sum
                