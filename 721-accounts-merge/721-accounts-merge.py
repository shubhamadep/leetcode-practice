
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []
        
        email_graph = collections.defaultdict(list)
        email_names = collections.defaultdict(str)
        
        for account in accounts:
            name = account[0]
            base_email = account[1]
            email_names[base_email] = name
            for email in account[2:]:
                email_graph[email].append(base_email)
                email_graph[base_email].append(email)
                email_names[email] = name
        
        visited = set()
        result = []
        
        for email in email_names:
            if email not in visited:
                queue = collections.deque()
                temp_result = []
                queue.append(email)
                visited.add(email)
                
                while queue:
                    node = queue.popleft()
                    temp_result.append(node)
                    for neighbor in email_graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                temp_result.sort()
                result.append([email_names[email]]+temp_result)
        
        return result
                
                
        
        