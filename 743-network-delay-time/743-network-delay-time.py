class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        #These are the libraries we will need
        import heapq
        import collections
        
        #Need to create an adjacency dictionary
        adj = collections.defaultdict(list)
        
        #We add nodes to our directed adj dictionary
        for n1, n2, weight in times:
            adj[n1].append((weight, n2))
            
        #We place the starting node with a time of zero
        heap = [(0, k)]
        #We don't want to visit the same node so we need to keep a set of visited
        visit = set()
        #We'll need to find the time for all the nodes to get a signal
        time = 0
        
        while heap:
            currWeight, currNode = heapq.heappop(heap)
            
            #If we've already visited, we continue
            if currNode in visit:
                continue
                
            #Add to visit
            visit.add(currNode)
            
            #We're going to check the time
            time = max(time, currWeight)
            
            #Now we need to check the neighbours
            for neiWeight, neiNode in adj[currNode]:
                heapq.heappush(heap, (neiWeight + time, neiNode))
                
        if len(visit) != n:
            return -1
        return time