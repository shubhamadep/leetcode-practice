class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def is_possible(val):
            res = 0
            for ribbon in ribbons:
                res += ribbon // val
                if res >= k:
                    return True
            return False
        
        #edge case
        if sum(ribbons) < k:
            return 0
        
        #binary search
        l, r = 1, max(ribbons)
        while l < r:
            mid = (l + r + 1) // 2
            if is_possible(mid):
                l = mid
            else:
                r = mid - 1
        return l
