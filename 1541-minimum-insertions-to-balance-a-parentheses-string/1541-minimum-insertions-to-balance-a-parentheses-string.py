class Solution:
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        
        s += "#"
        ob, cb = 0, 0
        i, j = 0, 0
        
        while i < len(s) - 1:
            if s[i] == '(':
                ob += 1
                i += 1
            else:
                if s[i] == ')' and s[i+1] == ')':
                    if ob:
                        ob -= 1
                    else:
                        cb += 1
                    i += 2
                
                if s[i] == ')' and s[i+1] != ')':
                    if ob:
                        ob -= 1
                        cb += 1
                    else:
                        cb += 2
                    
                    i += 1
                
        #some combination of ob and cb
        return cb + (ob*2)