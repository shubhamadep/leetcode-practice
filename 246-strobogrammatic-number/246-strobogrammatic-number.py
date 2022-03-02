class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        s_number = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        i, j = 0, len(num)-1
        
        while i <= j:
            if num[i] in s_number and num[j] in s_number:
                if s_number[num[i]] == num[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                return False
        
        return True
        