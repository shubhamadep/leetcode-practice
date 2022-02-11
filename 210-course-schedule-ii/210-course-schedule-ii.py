class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def generateIndegreeForNodes(numCourses, prerequisites):
            indegree = {}
            for i in range(numCourses):
                indegree[i] = 0
            for req, depReq in prerequisites:
                indegree[req] += 1
            return indegree
        
        def generateAdjListForNode(numCourse, prerequisites):
            adjList = collections.defaultdict(list)
            for req, depReq in prerequisites:
                adjList[depReq].append(req)
            return adjList
        
        def getZeroIndegreeNodes(indegree):
            nodes = []
            for node in indegree:
                if indegree[node] == 0:
                    nodes.append(node)
            return nodes
        
        indegree = generateIndegreeForNodes(numCourses, prerequisites)
        adjList = generateAdjListForNode(numCourses, prerequisites)
        stack = getZeroIndegreeNodes(indegree)
        result = []
        
        while stack:
            course = stack.pop()
            result.append(course)
            for dep in adjList[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    stack.append(dep)
        
        return result if len(result) == numCourses else []