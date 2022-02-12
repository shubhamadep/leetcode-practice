class FreqStack:

    def __init__(self):
        self.frequencies = collections.defaultdict(int)
        self.groups = collections.defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.frequencies[val] += 1
        f = self.frequencies[val]
        if f > self.maxFreq:
            self.maxFreq = f
        self.groups[f].append(val)
        
    def pop(self) -> int:
        val = self.groups[self.maxFreq].pop()
        self.frequencies[val] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return val
