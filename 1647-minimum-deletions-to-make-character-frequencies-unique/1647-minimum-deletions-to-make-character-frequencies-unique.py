class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        uniqueFreq = set()
        deletions = 0
        
        for k, v in freq.items():
            while v in uniqueFreq and v > 0:
                v -= 1
                deletions += 1
            uniqueFreq.add(v)
        
        return deletions
                