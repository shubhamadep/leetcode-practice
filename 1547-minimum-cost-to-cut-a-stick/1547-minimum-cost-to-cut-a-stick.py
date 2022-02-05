class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cache = {}
        def dp(start, end):
            if (start, end) in cache:
                return cache[(start, end)]
            res = float('inf')
            cost = end - start
            for cut in cuts:
                if start < cut < end:
                    res = min(res, dp(start, cut) + dp(cut, end) + cost)
            
            cache[(start, end)] = res if res != float('inf') else 0
            return cache[(start, end)]
        
        return dp(0, n)