class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        self.minimum_cost = 0
        def get_next_index(index, next_days):
            end = days[index] + next_days
            while index < len(days) and days[index] < end:
                index += 1
            return index
        
        memo = {}
        def helper(idx):
            if idx == len(days):
                return 0
            
            if idx in memo:
                return memo[idx]
            
            memo[idx] = min(helper(get_next_index(idx, 1))+costs[0], helper(get_next_index(idx, 7))+costs[1], helper(get_next_index(idx, 30))+costs[2])
            
            return memo[idx]
                                                                       
        return helper(0)