class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(start, end, find_first_occ):
            result = -1
            while start <= end:
                mid = end + (start - end) // 2
                
                if nums[mid] == target:
                    result = mid
                    if find_first_occ:
                        end = mid - 1
                    else:
                        start = mid + 1
                
                elif nums[mid] > target:
                    end = mid - 1
                
                else:
                    start = mid + 1
            
            return result
        
        first_occ = binary_search(0, len(nums)-1, True)
        if first_occ == -1:
            return [-1, -1]
        last_occ = binary_search(first_occ, len(nums)-1, False)
        return [first_occ, last_occ]