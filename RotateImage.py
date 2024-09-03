class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
        
        def reverseRows(matrix):
            for k in range(len(matrix)):
                left, right = 0, len(matrix) - 1
                while left < right:
                    matrix[k][left], matrix[k][right] = matrix[k][right], matrix[k][left]
                    left += 1
                    right -= 1

        transpose(matrix)
        reverseRows(matrix) 
        