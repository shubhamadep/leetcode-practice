class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        balance = 0
        count = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                if balance:
                    balance -= 1
                else:
                    count += 1
        
        return balance + count