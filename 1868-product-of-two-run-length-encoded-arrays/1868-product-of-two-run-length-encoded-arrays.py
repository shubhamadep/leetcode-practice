#TC: O(n)
#SC: O(1)
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        result = []
        
        e1 = 0
        e2 = 0
        
        while e1 < len(encoded1) and e2 < len(encoded2):
            
            value = encoded1[e1][0] * encoded2[e2][0]
            frequency = min(encoded1[e1][1], encoded2[e2][1])
            if result and result[-1][0] == value:
                result[-1][1] += frequency
            else:
                result.append([value, frequency])
            
            encoded1[e1][1] -= frequency
            encoded2[e2][1] -= frequency
            
            if encoded1[e1][1] == 0:
                e1 += 1
            if encoded2[e2][1] == 0:
                e2 += 1
            
        
        return result