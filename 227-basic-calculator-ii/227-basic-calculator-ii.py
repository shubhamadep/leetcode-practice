class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        number = 0
        
        def stack_handler(sign, number):
            if sign == '+':
                stack.append(number)
            elif sign == '-':
                stack.append(-number)
            elif sign == '*':
                stack[-1] *= number
            elif sign == '/':
                stack[-1] = int(stack[-1] / number)
        
        for char in s:
            if char.isdigit():
                number = (number * 10) + int(char)        
            elif char in ['+', '-', '*', '/']:
                stack_handler(sign, number)
                sign = char
                number = 0
        
        stack_handler(sign, number)
        
        return sum(stack)
                