'''

p - [[0,2],[5,10],[13,23],[24,25]]
1 - [[1,5],[8,12],[15,24],[25,26]]

stack = [[1,2]]

[x1, y1]
[x2, y2]

1. range -> [max(x1, x2), min(y1,y2)]

'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return  ans
                