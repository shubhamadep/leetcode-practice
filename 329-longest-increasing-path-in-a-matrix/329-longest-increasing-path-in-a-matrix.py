class Solution:
    def isValid(self, A, i, j):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, dp):
        ans = 0
        row = [1, 0, -1, 0]
        col = [0, 1, 0, -1]
        if dp[i][j]:
            return dp[i][j]
        else:
            for r, c in zip(row, col):
                nRow = i + r
                nCol = j + c
                if self.isValid(A, nRow, nCol) and A[i][j] > A[nRow][nCol]:
                    ans = max(ans, self.dfs(A, nRow, nCol, dp))

            dp[i][j] = 1 + ans
            return dp[i][j]

    def longestIncreasingPath(self, A):
        if not A:
            return 0

        m = len(A)
        n = len(A[0])
        dp =[[0]*n for _ in range(m)]
        return max(self.dfs(A, x, y, dp) for x in range(m) for y in range(n))