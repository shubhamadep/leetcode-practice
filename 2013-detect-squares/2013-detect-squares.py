class DetectSquares:

    def __init__(self):
        self.x = collections.defaultdict(set)
        self.points = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x[x].add(y)
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        
        for y in self.x[point[0]]:
            length = abs(y - point[1])
            if not length:
                continue
                
            for x in [point[0] + length, point[0] - length]:
                if (x, point[1]) in self.points and (x, y) in self.points:
                    res += self.points[(point[0], y)] * self.points[(x, point[1])] * self.points[(x, y)]
                    
        return res