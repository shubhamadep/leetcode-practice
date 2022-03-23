class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        graph=defaultdict(list)
        n=len(recipes)
        in_degree=defaultdict(int)
        for i in range(n):
            u=recipes[i]
            for v in ingredients[i]:
                graph[v].append(u)
                in_degree[u]+=1
        q=deque([i for i in supplies])
        while q:
            curr_supp=q.popleft()
            for nei in graph[curr_supp]:
                in_degree[nei]-=1
                if in_degree[nei]==0: q.append(nei)
        ans=[]
        for recipe in recipes:
            if in_degree[recipe]<=0: ans.append(recipe)
        return ans