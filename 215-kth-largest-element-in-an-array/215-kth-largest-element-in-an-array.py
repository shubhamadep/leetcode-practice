class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(nums, start, end, k):
            while True:
                pivot = start
                left = start + 1
                right = end
                while right >= left:
                    if nums[left] > nums[pivot] and nums[right] < nums[pivot]:
                        nums[left], nums[right] = nums[right], nums[left]
                    elif nums[left] <= nums[pivot]:
                        left += 1
                    elif nums[right] >= nums[pivot]:
                        right -= 1
                nums[pivot], nums[right] = nums[right], nums[pivot]
                if right == k:
                    return nums[right]
                elif k > right:
                    start = right+1
                else:
                    end = right-1
            return -1
                         
        if k > len(nums):
            return -1
        return helper(nums, 0, len(nums)-1, len(nums)-k)