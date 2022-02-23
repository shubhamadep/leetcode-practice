class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0]*(len(matrix[0])+1) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.dp[row][col+1] = self.dp[row][col] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2+1):
            sum += self.dp[row][col2+1] - self.dp[row][col1]
        
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)