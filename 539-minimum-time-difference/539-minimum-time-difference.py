'''

bucket sort: we know lower and higher ranges for minutes

0 - 1440 

so we add the times in buckets and just count sort it.

https://leetcode.com/problems/minimum-time-difference/discuss/1829297/python-3-bucket-sort-O(n)-time-O(1)-space

Algoexpert Radix sort video as well

'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        M = 1440
        times = [False] * M
        for time in timePoints:
            minute = self.minute(time)
            if times[minute]:
                return 0
            times[minute] = True
        
        minutes = [i for i in range(M) if times[i]]
        return min((minutes[i] - minutes[i-1]) % M for i in range(len(minutes)))
        
    def minute(self, time: str) -> int:
        h, m = map(int, time.split(':'))
        return 60*h + m