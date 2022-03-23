class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2==1:
            return []
        changed.sort()
        dic=defaultdict(int)
        for i in changed:
            dic[i]+=1
        

            
        res=[]
        for i in changed:
            if dic[i]>0:
                if dic[i*2]>0:
                    dic[i]-=1
                    dic[i*2]-=1
                    res.append(i)
                else:
                    return []
        return res