class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        row = matrix[0]
        for i in range(1,M):
            temp = matrix[i]
            for j in range(1,N):
                if row[j-1]!=temp[j]:
                    return False
            row = temp
        return True
