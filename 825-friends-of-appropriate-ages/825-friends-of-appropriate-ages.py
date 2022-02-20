class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        if len(ages) == 1:
            return 0
        
        self.counts = collections.defaultdict(int)
        
        def binary_search(ages, idx):
            start, end = 0, idx-1
            result = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                if 0.5 * ages[idx] + 7 >= ages[mid]: 
                    start = mid+1
                else:
                    end = mid-1
                    result = mid
                    
            if result != -1:
                return (idx - result) + self.counts[ages[idx]]
            
            return 0
                
        ages.sort()
        requests = 0
        for i in range(len(ages)):
            requests += binary_search(ages, i)
            self.counts[ages[i]] += 1
        
        return requests