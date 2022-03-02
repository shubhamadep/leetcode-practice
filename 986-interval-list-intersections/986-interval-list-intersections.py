class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i, j = 0, 0
        merged_set = []
        while i < len(firstList) and j < len(secondList):
            low_val = max(firstList[i][0], secondList[j][0])
            high_val = min(firstList[i][1], secondList[j][1])
            
            if low_val <= high_val:
                merged_set.append([low_val, high_val])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return merged_set