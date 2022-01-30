class Solution:
    def calculate(self, s: str) -> int:
        res, num = 0, 0
        stack = []
        sign = 1
        
        for c in s:
            
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c in ['+', '-']:
                res += sign*num
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ')':
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
                
        return res + num * sign