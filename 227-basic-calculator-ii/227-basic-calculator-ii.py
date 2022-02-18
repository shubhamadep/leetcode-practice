class Solution:
    def calculate(self, s: str) -> int:
        prevOperator = '+'
        stack = []
        number = 0
        
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                number = number*10 + int(char)
            if char in ['+', '-', '/', '*'] or i+1 == len(s):
                if prevOperator == '+':
                    stack.append(number)
                elif prevOperator == '-':
                    stack.append(-number)
                elif prevOperator == '/':
                    stack[-1] = int(stack[-1]/number)
                elif prevOperator == '*':
                    stack[-1] *= number
                number = 0
                prevOperator = char
        
        return sum(stack)
        