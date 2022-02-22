class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def last(days,index,plan):
            end = days[index] + plan
            while index!=len(days) and days[index] < end:
                index+=1
            return index

        def go(days,index,costs,dp):
            if index == len(days):
                return 0
            if dp[index] != -1:
                return dp[index]

            ans = min( costs[0] + go(days,last(days,index,1),costs,dp),
                       costs[1] + go(days,last(days,index,7),costs,dp),
                       costs[2] + go(days,last(days,index,30),costs,dp))

            dp[index] = ans
            return ans

        dp = [-1]*len(days)
        return go(days,0,costs,dp)
