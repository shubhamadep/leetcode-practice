'''

ba ll oon
11 2  2 1

'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dictionary = collections.Counter(text)
        pattern = 'balloon'
        pattern_dictionary = collections.Counter(pattern)
        
        min_count = float('inf')
        for char in 'balloon':
            if char not in dictionary:
                return 0
            min_count = min(min_count, dictionary[char] // pattern_dictionary[char])
        
        return min_count