class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = float('-inf')
        result = []
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]
            if height > maxHeight:
                maxHeight = height
                result.append(i)
        return result[::-1]