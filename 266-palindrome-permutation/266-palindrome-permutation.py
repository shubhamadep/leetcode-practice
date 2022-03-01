class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        seen = collections.Counter(s)
        is_even = len(s) % 2 == 0
        
        if is_even: 
            for char in seen:
                if seen[char] % 2 != 0:
                    return False
        else:
            odd = 0
            for char in seen:
                if seen[char] % 2 == 0:
                    continue 
                if odd == 0:
                    odd += 1
                else:
                    return False
        return True