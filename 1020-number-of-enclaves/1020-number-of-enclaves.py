class Solution:
    def numEnclaves(self, A):
        count = 0
        def dfs(i, j):
            A[i][j] = 2
            for a, b in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                row = i + a
                col = j + b
                if 0 <= row < len(A) and 0 <= col < len(A[0]) and A[row][col] == 1:
                    dfs(row, col)
            
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i == 0 or i == len(A) - 1 or j == 0 or j == len(A[0]) - 1) and A[i][j] == 1:
                    dfs(i, j)
                    
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    count += 1
        
        return count