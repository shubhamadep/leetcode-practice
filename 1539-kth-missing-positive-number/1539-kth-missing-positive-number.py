class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set()
        for num in arr:
            seen.add(num)
        
        for i in range(1, arr[-1]+1):
            if i not in seen:
                k -= 1
            if k == 0:
                return i
        
        return arr[-1]+k