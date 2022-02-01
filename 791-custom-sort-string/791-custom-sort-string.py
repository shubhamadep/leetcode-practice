class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = collections.Counter(list(s))
        result = ""
        for char in order:
            if char in counts:
                result += counts[char] * char
                counts[char] = 0
        
        print(counts)
        for char in counts:
            if counts[char] != 0:
                result += counts[char] * char
        
        return result