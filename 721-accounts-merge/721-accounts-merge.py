'''
[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

"johnsmith@mail.com" -> (0)
merged_set  = (0, 2)
sorting = logn

Graph problem

'''
from collections import defaultdict, deque
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        if not accounts:
            return []
        
        email_name = defaultdict(str)
        emails = defaultdict(list)
        
        for acc in accounts:
            name = acc[0]
            base = acc[1]
            email_name[base] = name
            for em in acc[2:]:
                emails[base].append(em)
                emails[em].append(base)
                email_name[em] = name
        
        visited= set()
        result = []
        for en in email_name:
            if en not in visited:
                
                current_result = []
                current_result.append("")
                q = deque([en])
                visited.add(en)
                
                while q:
                    email = q.popleft()
                    current_result.append(email)
                    for em in emails[email]:
                        if em not in visited:
                            visited.add(em)
                            q.append(em)
                
                current_result.sort()
                current_result[0] = email_name[en]
                result.append(current_result)
        
        return result
            
        