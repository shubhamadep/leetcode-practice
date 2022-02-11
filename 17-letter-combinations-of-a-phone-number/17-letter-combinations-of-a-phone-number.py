class Solution(object):
    def letterCombinations(self, digits):
        
        if not digits:
            return []
        
        result = []
        mappings = {
                '0' : ['0'],
                '1' : ['1'],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        self.getLetterCombinations(result, digits, "", 0, mappings)
        return result
    
    def getLetterCombinations(self, result, digits, current, index, mappings):
        if index == len(digits):
            result.append(current)
            return
        
        children = mappings[digits[index]]
        for child in children:
            self.getLetterCombinations(result, digits, current + child, index+1, mappings)