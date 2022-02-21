#TC: O(n)
#SC: O(n)

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        
        stack = []
        result = [0] * len(heights)
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            while stack and height > stack[-1]:
                stack.pop()
                result[i] += 1
            
            if stack:
                result[i] += 1
            
            stack.append(height)
            
        return result