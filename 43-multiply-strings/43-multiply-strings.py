class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1 == '0' or num2 == '0':
            return '0'
        
        result = [0] * (len(num1) + len(num2))
        
        number1 = num1[::-1]
        number2 = num2[::-1]
        
        
        for i, n2 in enumerate(number2):
            for j, n1 in enumerate(number1):
                zeroes = i+j
                
                carry = result[zeroes]
                number = int(n1) * int(n2) + carry
                
                
                result[zeroes] = number % 10
                result[zeroes + 1] += number //10
        
        
        if result[-1] == 0:
            result.pop()
        
        
        final_result = ""
        for n in reversed(result):
            final_result += str(n)
        
        return final_result