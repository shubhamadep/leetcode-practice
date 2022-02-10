'''
the sky is blue
012345678901234
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        if s.count(" ") == 0:
            return s
        else:
            s = s.split()
            s = " ".join(s)
        
            stack = []
            subs = ""    

            for i in range(len(s)-1, -1, -1):
                if s[i].isalnum():
                    subs = s[i] + subs
                else:
                    stack.append(subs)
                    subs = ""
            stack.append(subs) if subs else ""
        return " ".join(stack)
    
                