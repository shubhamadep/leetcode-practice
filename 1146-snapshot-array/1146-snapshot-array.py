class SnapshotArray:
    
    def __init__(self, length: int):
        self.hmap=defaultdict()
        for i in range(length):
            self.hmap[i]=[[-1, 0]]
                #snap id   #value
        self.snap_id=0
        
    def set(self, index: int, val: int) -> None:
        self.hmap[index].append([self.snap_id, val])
        
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
    
        i = bisect.bisect(self.hmap[index], [snap_id + 1]) - 1
        return self.hmap[index][i][1] 