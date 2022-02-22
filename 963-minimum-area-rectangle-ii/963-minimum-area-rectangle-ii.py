from typing import List, Tuple
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # key: for rect, diagonals from corners will:
        # 1) intersect at common midpoint
        # 2) and be of equal length

        # going through and comparing two points:
        # calculate distance between points (hello math)
        # calculate midpoint between points (hello math)
        # store in dict {(mid, dist) : [(pairs)]}

        # then go through dict keys with len > 1
        # compare points against each other,
        # calc distance between pair1 point1 and pair2 both points
        # product of these distances == area
        # track for min area
        # O(N^2) time and O(N) space

        def get_dist(p1, p2) -> float:
            x1,y1 = p1
            x2,y2 = p2
            return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

        def get_mid(p1, p2) -> Tuple[float, float]:
            x1,y1 = p1
            x2,y2 = p2
            return ((x1+x2)/2, (y1+y2)/2)

        d = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                mid = get_mid(points[i], points[j])
                dist = get_dist(points[i], points[j])
                d[(mid, dist)].append( (points[i], points[j]) )

        res = float("inf")
        for k in d:
            if len(d[k]) > 1:
                for i in range(len(d[k])):
                    for j in range(i+1, len(d[k])):
                        p1, p2 = d[k][i]
                        p3, p4 = d[k][j]

                        side1 = get_dist(p1,p3)
                        side2 = get_dist(p1,p4)
                        res = min(res, side1 * side2)

        return res if res < float("inf") else 0