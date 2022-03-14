class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        num = 0
        
        for char in s:
            if char.isdigit():
                num = (num*10) + int(char)
            
            elif char == "[":
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
                
            elif char == ']':
                prev_count = stack.pop()
                prev_string = stack.pop()
                string =  prev_string + prev_count*string 
            
            else:
                string = string + char
    
        return string 