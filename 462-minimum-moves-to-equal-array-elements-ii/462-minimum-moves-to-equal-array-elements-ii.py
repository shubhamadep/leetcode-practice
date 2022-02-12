class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def partition(arr, l, r):
            random_i = random.randint(l, r)
            arr[l], arr[random_i] = arr[random_i], arr[l]
            pivot, j = arr[l], l
            for i in range(l + 1, r + 1):
                if arr[i] < pivot:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            return j
        
        n = len(nums)
        l, r, median_index = 0, n - 1, n >> 1
        
        while True:
            index = partition(nums, l, r)
            if index < median_index:
                l = index + 1
            elif index > median_index:
                r = index - 1
            else:
                break
        
        return sum(abs(num - nums[median_index]) for num in nums)
    
# class Solution:
    
#     def kthelement(self, array, start, end, k):
#         while True:
#             if start > end:
#                 return
#             pivot = start
#             left = start+1
#             right = end
#             while right >= left:
#                 if array[right] < array[pivot] and array[left] > array[pivot]:
#                     array[right], array[left] = array[left], array[right]
#                 elif array[right] >= array[pivot]:
#                     right -= 1
#                 elif array[left] <= array[pivot]:
#                     left += 1
#             array[right], array[pivot] = array[pivot], array[right]
#             if right == k:
#                 return right
#             elif right < k:
#                 start = right + 1
#             else:
#                 end = right - 1
                
#     def minMoves2(self, nums: List[int]) -> int:
#         median_index = self.kthelement(nums, 0, len(nums)-1, len(nums) // 2)
#         return sum(abs(num - nums[median_index]) for num in nums)