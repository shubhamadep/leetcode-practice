class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        
        i = 0
        while i < len(s)-1:
            if s[i] < s[i+1]:
                break
            i += 1
            
        if i == len(s) - 1:
            return num
        
        max_idx, max_val = i+1, s[i+1]
        for j in range(i+1, len(s)):
            if s[j] >= max_val:
                max_val = s[j]
                max_idx = j
        
        min_idx = i
        for j in range(i, -1, -1):
            if s[j] < max_val:
                min_idx = j
        
        s[min_idx], s[max_idx] = s[max_idx], s[min_idx]
        return int(''.join(s))