class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        #edge cases
        if not prerequisites:
            return numCourses
        
        #adjecency list
        adj, indegree = collections.defaultdict(list), {}
        count = 0
        
        for i in range(numCourses):
            indegree[i] = 0
    
        #indegree, and adj matrices of courses
        for i in range(len(prerequisites)):
            
            c, d = prerequisites[i]
            adj[d].append(c)
            indegree[c] = indegree.get(c) + 1

        stack = []
        for k in indegree:
            if indegree[k] == 0:
                stack.append(k)

        while stack:
            count += 1
            top = stack.pop()
            print(top)
            for neighbor in adj[top]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: 
                    stack.append(neighbor)
        
        return count == numCourses