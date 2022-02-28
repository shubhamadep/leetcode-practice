#TC: O(nk)
#SC: O(nk)
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        countmap = defaultdict(list)
        if not strings:
            return []
    
        for s in strings:
            
            length = len(s)
            key = []
            
            for i in range(1, length):
                key.append(((ord(s[i]) - ord(s[i-1])) % 26))
            
            countmap[str(key)].append(s)
        
        
        result = []
        
        for k in countmap:
            result.append(countmap[k])
        
        return result