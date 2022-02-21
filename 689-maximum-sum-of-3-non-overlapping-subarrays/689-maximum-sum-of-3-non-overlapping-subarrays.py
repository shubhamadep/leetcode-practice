class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        memo = {}
        res = self.window_sum(nums, k, 0, 0, memo)
        return res[1]

    def window_sum(self, nums, k, idx, used, memo):
        # we can only have 3 windows at a time
        if used == 3:
            return 0, []

        # are we going to overflow over our nums array?
        if idx - (used * k) > (len(nums)):
            return 0, []

        if (idx, used) in memo:
            return memo[(idx, used)]

        take_curr_sum, take_curr_indices = self.window_sum(nums, k, idx + k, used + 1, memo)
        take_curr_sum += sum(nums[idx:idx + k])

        skip_curr_sum, skip_curr_indices = self.window_sum(nums, k, idx + 1, used, memo)

        if take_curr_sum >= skip_curr_sum:
            memo[(idx, used)] = (take_curr_sum, ([idx] + take_curr_indices))
            return memo[(idx, used)]
        else:
            memo[(idx, used)] = (skip_curr_sum, skip_curr_indices)
            return memo[(idx, used)]