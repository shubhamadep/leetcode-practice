class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d={'a':a,'b':b,'c':c}
        h=[]
        for k,v in d.items():
            if v>0:
                heapq.heappush(h,(-v,k))
        res=''
        while h:
            top=heapq.heappop(h)
            if len(res)>1 and top[1]*2==res[-2:]:
                if not h:
                    break
                second=heapq.heappop(h)
                heapq.heappush(h,(-d[top[1]],top[1]))
                top=second
            res+=top[1]
            d[top[1]]-=1
            if d[top[1]]>0:
                heapq.heappush(h,(-d[top[1]],top[1]))
                
        return res