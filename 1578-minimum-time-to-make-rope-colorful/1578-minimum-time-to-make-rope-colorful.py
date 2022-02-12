class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s_it = 0
        res = 0
        heap = []
        
        while s_it < len(s):
            heapq.heappush(heap, cost[s_it])
            while s_it < len(s) - 1 and s[s_it] == s[s_it + 1]:
                heapq.heappush(heap, cost[s_it + 1])
                s_it += 1
            
            while len(heap) > 1:
                res += heapq.heappop(heap)
            
            heap = []
            s_it += 1
        
        return res