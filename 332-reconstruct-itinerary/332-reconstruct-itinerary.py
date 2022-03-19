'''
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
'''
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def backtrack(node, path):
            if len(path) == total_flights:
                self.result = path
                return True
            
            for i, destination in enumerate(origin_destination[node]):
                if not visited[node][i]:
                    visited[node][i] = True
                    exists = backtrack(destination, path+[destination])
                    visited[node][i] = False
                    if exists:
                        return True
            
            return False
        
        origin_destination = collections.defaultdict(list)
        for ticket in tickets:
            origin_destination[ticket[0]].append(ticket[1])
            
        visited = collections.defaultdict(list)
        for airport in origin_destination:
            destination = origin_destination[airport]
            origin_destination[airport].sort()
            visited[airport] = [False]*len(destination)
        
        start_airport = 'JFK'
        path = ['JFK']
        total_flights = len(tickets)+1
        self.result = []
        backtrack(start_airport, path)
        
        return self.result