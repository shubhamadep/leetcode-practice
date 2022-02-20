class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = collections.Counter(t)
        T = len(t)
        left, right = 0, 0
        min_window = ""
        min_window_lenght = float('inf')
        count = 0
        
        while right < len(s):
            char = s[right]
            if char in t_count:
                if t_count[char] > 0:
                    count += 1
                t_count[char] -= 1
            
            while count == T:
                current_window = right - left + 1
                if current_window < min_window_lenght:
                    min_window_lenght = current_window
                    min_window = s[left:right+1]
                
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] > 0:
                        count -= 1
                
                left += 1
            right += 1
        
        return min_window
        
        