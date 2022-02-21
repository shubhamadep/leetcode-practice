class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        curr_count = 0
        s_len= len(s)
        stack.append(["s[0]",0])
        for ch in s:
            
            if stack[-1][0] == ch:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
            
        result = ""
        for st in stack:
            if st[0] == "s[0]":
                continue
           
            result += st[0] * st[1]
        return result