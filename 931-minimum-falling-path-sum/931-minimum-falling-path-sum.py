class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for row in range(1, len(matrix)):
            
            for col in range(len(matrix[0])):
                
                upLeft = matrix[row - 1][col - 1] if col - 1 >= 0 else math.inf
                up = matrix[row - 1][col]
                upRight = matrix[row - 1][col + 1] if col + 1 < len(matrix)  else math.inf 

                currMin = matrix[row][col] + min(upLeft, up, upRight)
    
                matrix[row][col] = currMin;
        
        return min(matrix[len(matrix) - 1])