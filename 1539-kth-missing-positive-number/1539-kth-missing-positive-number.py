class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        
        while left <= right:
            mid = left + ( right - left ) // 2
            missing_on_left = arr[mid] - mid - 1
            
            if missing_on_left < k:
                left = mid+1
            else:
                right = mid-1
        
        # this can also translate to left + k as left = right + 1 after binary search
        return arr[right] + k - (arr[right] - right - 1)